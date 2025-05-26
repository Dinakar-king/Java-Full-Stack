from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse 
from PIL import Image
from io import BytesIO
from imageclassifier import predict_image
from sentiment import analyze_sentiment

app = FastAPI(title="Image classfier API", version="1.0")

@app.post("/predict")
async def predict(file: UploadFile=File(...)):
    if not file.content_type.startswith('image/'):
        return JSONResponse(status_code=400,content={"error": "File is not an image"})
    
    contents = await file.read()
    image =Image.open(BytesIO(contents)).convert("RGB")
    
    label, confidence =predict_image(image)
    return {"label" : label, "confidence":confidence}
@app.post("/sentiment")
async def predict_sentiment(text: str):
    print(text)
    return analyze_sentiment(text)