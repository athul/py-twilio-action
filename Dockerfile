FROM python:3.7-slim
ADD app.py /app
WORKDIR /app
RUN pip install twilio
CMD ["python", "/app/app.py"]
