FROM python:latest
ADD  app.py /app.py
RUN pip install twilio
CMD python app.py
