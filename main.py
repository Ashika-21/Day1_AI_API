from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class GenerateRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "AI API is running with Gemma"}


@app.post("/generate")
def generate(request: GenerateRequest):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": request.text,
            "stream": False
        }
    )

    result = response.json()

    return {
        "input": request.text,
        "response": result["response"]
    }
