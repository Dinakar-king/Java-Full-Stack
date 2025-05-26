import models
import database
import schemas
from fastapi import FastAPI, status, Depends, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
import os
import uvicorn # Make sure uvicorn is imported if used in _main_
import google.generativeai as genai
from dotenv import load_dotenv
from pdfminer.high_level import extract_text

load_dotenv() # Load environment variables from .env file

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title="Job_Course_Recommendation")

# Configure Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not found in environment variables. Job suggestion endpoint will not work.")
    # raise ValueError("GOOGLE_API_KEY not found in environment variables.") # Or raise an error
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Placeholder for resume parsing logic (implementation is out of scope for this request)
def extract_data_from_resume(file_path: str) -> str:
    """Extracts text data from a resume file."""
    # In a real application, this function would use a library like pdfminer, python-docx, etc.
    # For now, it will return a placeholder or raise NotImplementedError.
    print(f"Placeholder: Would extract data from {file_path}")
    # Example: return "Experienced Python developer with skills in FastAPI and SQL."
    try:
        with open(file_path, 'r') as f: # Try reading as text for simplicity
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path} in placeholder: {e}")
        return "Could not extract resume content."

def extract_data_from_resume_pdf(file_path: str) -> str:
    try:
        text = extract_text(file_path)
        return text if text.strip() else "No extractable text found."
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return "Resume parsing failed."


@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/parsing/{user_id}") # Added user_id to associate resume with a user
async def resume_parsing(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    temp_dir = "temp_resumes"
    os.makedirs(temp_dir, exist_ok=True)
    file_location = os.path.join(temp_dir, f"user_{user_id}_{file.filename}")
    
    try:
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        extracted_data = extract_data_from_resume_pdf(file_location)
        print(extracted_data)
        
        # Update user's resume in the database
        db_user.resume = extracted_data
        db.commit()
        db.refresh(db_user)
        
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
            
    return JSONResponse(content={"message": "Resume parsed and saved successfully", "user_id": user_id, "extracted_text_preview": extracted_data[:200] + "..."})

@app.post("/suggest_job/{user_id}", response_model=schemas.JobSuggestion)
async def suggest_job_title(user_id: int, db: Session = Depends(get_db)):
    if not GOOGLE_API_KEY:
        raise HTTPException(status_code=500, detail="Google API Key not configured. Cannot suggest job.")

    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not db_user.resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found for this user. Please upload and parse a resume first.")

    try:
        model = genai.GenerativeModel('gemini-2.0-flash') # Using a known available model
        prompt = f"Based on the following resume, suggest a suitable job title. Provide only the job title as a string:\n\nResume:\n{db_user.resume}"
        response = await model.generate_content_async(prompt)
        
        # Ensure response.text is accessed correctly
        job_title = response.text.strip()
        
        return schemas.JobSuggestion(suggested_title=job_title, user_id=user_id)
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get job suggestion from AI model: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)