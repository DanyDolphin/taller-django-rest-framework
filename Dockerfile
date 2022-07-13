# base image
FROM python:3.8

# setting work directory
RUN mkdir -p app
WORKDIR /app

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# installing dependencies
RUN pip install --upgrade pip

# copying whole project
COPY . /app

# installing project dependencies
RUN pip install -r requirements.txt

# exposing port
EXPOSE 8000

# starting server
CMD python manage.py runserver 0.0.0.0:8000