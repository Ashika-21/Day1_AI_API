# Day 1 - AI API using FastAPI

## About the Project

This project demonstrates how an AI capability can be exposed through a FastAPI backend.

The application accepts a text input from the user and processes it using a simple Python-based AI function.

## Workflow

User Input
↓
POST /generate
↓
FastAPI Backend
↓
AI Processing
↓
JSON Response

## Technologies Used

- Python
- FastAPI
- Uvicorn

## API Endpoint

### POST /generate

The user sends a text input to the API.

Example request:

{
    "text": "Explain artificial intelligence in simple terms"
}

Example response:

{
    "input": "Explain artificial intelligence in simple terms",
    "response": "Artificial Intelligence is the ability of computers to perform tasks that normally require human intelligence."
}

## How to Run

Install the required packages:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs

## Project Structure

Day1_AI_API/
│
├── main.py
├── requirements.txt
├── README.md
