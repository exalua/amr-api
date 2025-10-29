from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = {}  # In-memory store for user Robocons

class AddCashRequest(BaseModel):
    username: str
    amount: int

@app.post("/add_cash")
async def add_cash(req: AddCashRequest):
    username = req.username.lower()
    data[username] = data.get(username, 0) + req.amount
    return {"message": f"Added {req.amount} cash to {username}", "total_cash": data[username]}

@app.get("/get_cash")
async def get_cash(username: str):
    username = username.lower()
    return {"username": username, "cash": data.get(username, 0)}

# ✅ Add this /pending endpoint
@app.get("/pending")
async def pending():
    return data
