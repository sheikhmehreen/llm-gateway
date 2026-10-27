from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LLM Gateway")


class ChatRequest(BaseModel):
    message: str
    provider: str = "groq"


class ChatResponse(BaseModel):
    message: str
    provider: str
    status: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        message="Mock response",
        provider=request.provider,
        status="success",
    )