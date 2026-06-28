FROM python:3.9-slim

WORKDIR /app

COPY app.py . 

CMD ["sh", "-c", "python app.py && tail -f /dev/null"]
