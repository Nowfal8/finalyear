from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (HTML) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data API
@app.get("/data")
def get_data():
    return {"heart_rate": 85, "motion": 2.3}

# Receive data (ESP32)
@app.post("/data")
def receive_data(data: dict):
    return {"status": "received", "data": data}
