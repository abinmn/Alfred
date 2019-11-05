  
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 8 Alfred.wsgi:application