FROM python:3.10-slim

WORKDIR /app

COPY client.py .
COPY client.crt .
COPY client.key .
COPY ca.crt .

CMD ["python", "client.py"]

