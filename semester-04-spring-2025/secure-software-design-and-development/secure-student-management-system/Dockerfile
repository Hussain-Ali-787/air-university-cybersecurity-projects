FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY .env.example .env.example

ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV PORT=5000

EXPOSE 5000

CMD ["sh", "-c", "python src/create_db.py && exec python src/app.py"]
