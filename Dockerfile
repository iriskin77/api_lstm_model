FROM python:3.10-slim

WORKDIR /file

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x ./celery_worker.sh
RUN chmod a+x ./start.sh
