import logging
import time
import httpx
from fastapi import FastAPI
from opentelemetry import trace

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] %(message)s",
)
logger = logging.getLogger("checkout-api")

app = FastAPI()

@app.get("/checkout")
async def checkout():
    logger.info("Processing checkout request")
    time.sleep(0.15)
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://localhost:8000/inventory")
    logger.info("Checkout completed successfully")
    return {"status": "order_placed", "inventory": resp.json()}

@app.get("/inventory")
async def inventory():
    logger.info("Checking inventory stock")
    time.sleep(0.05)
    return {"in_stock": True}
