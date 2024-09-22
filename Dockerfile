FROM --platform=linux/amd64 python:3.10-alpine as build

RUN mkdir /app
WORKDIR /app
COPY ./src/ .
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

CMD python3 main.py -n 3