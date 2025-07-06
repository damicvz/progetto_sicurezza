FROM python:3.10-slim

WORKDIR /app

COPY server.py .
COPY server.crt .
COPY server.key .
COPY ca.crt .

CMD ["python", "server.py"]

