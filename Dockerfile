FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "contact_manager.py"]