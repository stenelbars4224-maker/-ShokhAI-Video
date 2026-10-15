
from fastapi import FastAPI

app = FastAPI(title="ShokhAI-Video API")


@app.get("/")
def home():
    return {"status": "ShokhAI-Video server ishlayapti"}
