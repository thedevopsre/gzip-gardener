FROM python:3.9-slim

WORKDIR /usr/src/app

COPY backup_cleanup.py .

CMD ["python3", "./backup_cleanup.py"]