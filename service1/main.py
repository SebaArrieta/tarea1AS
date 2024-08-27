from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

app = FastAPI()

logging.basicConfig(filename='/var/log/service1/app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

songs_db = [
    {
        'name': 'All I Need',
        'artist': 'Radiohead'
    },
    {
        'name': 'Sleep',
        'artist': 'My Chemical Romance'
    },
    {
        'name': 'Love, Hate, Love',
        'artist': 'Alice in Chains'
    }
]

class Song(BaseModel):
    name: str
    artist: str

@app.get('/{id}', response_model=Song)
async def index(id: int):
    try:
        logger.info("Service 1 - request")
        return songs_db[int(id)]
    except:
        raise HTTPException(status_code=404, detail="Song not found")
