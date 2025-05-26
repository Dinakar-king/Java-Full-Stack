from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    new_message: str

class ChatResponse(BaseModel):
    message: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        api_key = ("AIzaSyDYlLPKXjcrvyTMl8ANYH_FgvKM1mrIdcM")
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not configured")
            
        client = genai.Client(api_key=api_key)
        
        # Prepare conversation history
        conversation_history = []
        for msg in request.messages:
            conversation_history.append({
                "role": msg.role,
                "parts": [{"text": msg.content}]
            })
        
        # Add new user message
        conversation_history.append({
            "role": "user",
            "parts": [{"text": request.new_message}]
        })
        
        # Get response from Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=conversation_history
        )
        
        return ChatResponse(message=response.text)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
