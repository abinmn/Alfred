FROM python:3.5.7-slim-buster

WORKDIR /app
COPY DjangoApp/src /app
COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver"]