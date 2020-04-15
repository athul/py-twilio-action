FROM python:latest
RUN pip install twilio
CMD python app.py
