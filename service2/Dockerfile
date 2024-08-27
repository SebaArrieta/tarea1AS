FROM python:3.8-slim
WORKDIR /code

RUN mkdir -p /var/log/service2

COPY requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /code/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .
CMD ["uvicorn", "service2.main:app", "--reload", "--host", "0.0.0.0", "--port", "8001", "--reload"]
