FROM python:3.10-slim

RUN mkdir /file

WORKDIR /file

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN aerich upgrade


#RUN uvicorn main:app --reload --host 0.0.0.0 --port 8000
CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
