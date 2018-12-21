FROM python:3.7-alpine

WORKDIR /app
ADD . .

ENTRYPOINT [ "python", "/app/index.py"]