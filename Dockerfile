FROM python:3.10-slim

RUN mkdir /file

WORKDIR /file

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN aerich upgrade

WORKDIR apps

RUN uvicorn main:app --reload --host 0.0.0.0 --port 8090
