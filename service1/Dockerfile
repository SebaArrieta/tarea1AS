FROM python:3.8-slim
WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /code/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .
CMD ["uvicorn", "service1.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]