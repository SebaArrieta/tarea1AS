from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get('/getSong/{id}')
async def index(id: int):
    #try:
    response = httpx.get(f"http://service1:8000/{id}")
    message = response.json()
    return message
    #except:
        #raise HTTPException(status_code=500, detail="Server error")

#docker-compose down; docker-compose up --build --remove-orphans

"""
FROM python:3.8-slim
WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /code/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .
CMD ["uvicorn", "service2.main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]

"""
