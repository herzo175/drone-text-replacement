FROM python:3.7-alpine

WORKDIR /app
ADD . .

CMD ["python", "index.py"]