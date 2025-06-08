FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y e2fsprogs && \
    chmod -R 444 /app && \
    find /app -type f -exec chattr +i {} \;

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
