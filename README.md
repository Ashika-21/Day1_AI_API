# Day 1 - AI API using FastAPI and Gemma 2B

## Project Description

This project demonstrates how to build a simple AI application using FastAPI and a local Large Language Model (LLM).

The application accepts a user's text input through a REST API endpoint. FastAPI sends the input to Ollama, which runs the Gemma 2B language model locally. The generated response is then returned to the user in JSON format.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Ollama
- Gemma 2B
- Requests
- REST API
- JSON

## Project Workflow

The application follows this workflow:

User
↓
POST /generate
↓
FastAPI Backend
↓
Ollama API
↓
Gemma 2B LLM
↓
Generated Response
↓
FastAPI
↓
JSON Response

## API Endpoint

### POST /generate

This endpoint accepts a text input from the user and generates a response using the Gemma 2B language model.

### Example Request

```json
{
  "text": "Explain artificial intelligence in simple terms"
}
