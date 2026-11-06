from fastapi import FastAPI

app = FastAPI(title="Ask API")

@app.get("/")
def home():
    return {"message": "Hello from my first API"}

@app.get("/health")
def health():
    return {"status": "ok"}