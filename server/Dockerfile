FROM python:3.11.0-alpine3.17

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

# pip freeze > requirements.txt

# Install your application dependencies
RUN pip install -r requirements.txt