from fastapi import FastAPI, Request, UploadFile, File, Form
from chatgpt import ask_to_chatgpt
from consume_ocr import call_ocr_service
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    img_text = await call_ocr_service(file)
    print(img_text)
    answer = ask_to_chatgpt(img_text)
    obligations = answer.split("|")
    return templates.TemplateResponse("obligations.html", {"request": request, "obligations": obligations})
