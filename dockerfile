FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libpq-dev

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]