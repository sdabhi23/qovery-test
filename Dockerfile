FROM python:3.7

COPY . /app

WORKDIR /app

RUN apt-get update \
    && apt-get install -y wget

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run