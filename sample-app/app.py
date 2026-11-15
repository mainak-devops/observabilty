import time
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/checkout")
async def checkout():
    time.sleep(0.15)
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://localhost:8000/inventory")
    return {"status": "order_placed", "inventory": resp.json()}

@app.get("/inventory")
async def inventory():
    time.sleep(0.05)
    return {"in_stock": True}
