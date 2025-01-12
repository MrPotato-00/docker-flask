FROM python:3.10

WORKDIR /app

COPY flaskapp.py /app/
COPY script.py /app/
COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["python3", "/app/flaskapp.py"] 
