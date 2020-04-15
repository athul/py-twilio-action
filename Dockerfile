FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install --target=/app twilio
CMD ["python", "/app/app.py"]
