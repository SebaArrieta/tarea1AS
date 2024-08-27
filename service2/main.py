from fastapi import FastAPI, HTTPException
import httpx
import logging

app = FastAPI()

logging.basicConfig(filename='/var/log/service2/app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/getSong/{id}')
async def index(id: int):
    try:
        response = httpx.get(f"http://service1:8000/{id}")
        message = response.json()
        return message
    except:
        raise HTTPException(status_code=500, detail="Server error")
