import fastapi as FastAPI
import uvicorn as Uvicorn

app = FastAPI.FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def get_health():
    return {"status": "healthy"}

if __name__ == "__main__":
    Uvicorn.run(app, host="0.0.0.0", port=8000)
