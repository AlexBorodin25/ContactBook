FROM python:3.12-slim

WORKDIR /app

COPY contact_manager.py .

CMD ["python", "contact_manager.py"]