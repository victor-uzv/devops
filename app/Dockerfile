FROM python:3.7-alpine

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY app/ /app
WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["python3.7", "api.py"]
