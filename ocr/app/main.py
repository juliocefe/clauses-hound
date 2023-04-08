from fastapi import FastAPI, UploadFile
from images_processor import process_image

app = FastAPI()

@app.post("/process_image/")
async def process_image_view(file: UploadFile):
    # Save file locally
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    print("ARCHIVO", file.filename)
    text = process_image(file.filename)
    return {"text": text}