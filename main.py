from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GenerateRequest(BaseModel):
    text: str


def ai_response(text):
    text = text.lower()

    if "artificial intelligence" in text or "ai" in text:
        return "Artificial Intelligence is the ability of computers to perform tasks that normally require human intelligence."

    elif "machine learning" in text:
        return "Machine Learning is a method where computers learn patterns from data and use them to make predictions."

    elif "python" in text:
        return "Python is a popular programming language used for web development, data science, machine learning and AI."

    else:
        return "I received your question and processed it using the AI application."


@app.get("/")
def home():
    return {"message": "AI API is running"}


@app.post("/generate")
def generate(request: GenerateRequest):
    user_input = request.text

    response = ai_response(user_input)

    return {
        "input": user_input,
        "response": response
    }