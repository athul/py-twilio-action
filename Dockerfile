FROM python:latest
COPY app.py app.py
RUN pip install twilio
CMD "python" "./app.py"
