from fastapi import UploadFile
import requests

async def call_ocr_service(file: UploadFile):
    url = "http://ocr:5000/process_image/"

    # Save file locally
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    # Send file to another service
    with open(file.filename, "rb") as buffer:
        files = {"file": buffer}
        r = requests.post(url, files=files)
    text = r.json()["text"]
    return text