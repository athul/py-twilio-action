FROM python:3.7-slim
ADD . /app
WORKDIR /app
RUN pip install --target=/app twilio
RUN chmod +x /app/app.py
CMD ["python", "/app/app.py"]
