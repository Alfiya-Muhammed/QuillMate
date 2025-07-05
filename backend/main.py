from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.chains import enhance_style, generate_text, analyze_tone, expand_text
from backend.style_index import build_user_index, generate_with_style

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    mode: str
    input_text: str
    genre: str = ""
    style: str = ""
    tone: str = ""

@app.post("/generate/")
def generate(request: PromptRequest):
    return generate_text(request)

@app.post("/analyze/")
def analyze(request: PromptRequest):
    return analyze_tone(request)

@app.post("/expand/")
def expand(request: PromptRequest):
    return expand_text(request)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    try:
        content = await file.read()
        filename = f"data/user_writings/{file.filename}"
        with open(filename, "wb") as f:
            f.write(content)
        try:
            build_user_index(filename)
            return {"status": "uploaded and indexed successfully"}
        except Exception as e:
            return {"status": f"uploaded but indexing failed: {str(e)}"}
    except Exception as e:
        return {"status": f"upload failed: {str(e)}"}

# @app.post("/style_generate/")
# def style_generate(request: PromptRequest):
#     return generate_with_style(request.input_text)

@app.post("/enhance/")
def enhance(request: PromptRequest):
    return enhance_style(request)
