from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
        return songs_db[int(id)]
    except:
        raise HTTPException(status_code=404, detail="Song not found")
