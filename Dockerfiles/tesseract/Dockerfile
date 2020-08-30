FROM ubuntu:20.04
LABEL author="akempler@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-add-repository universe
RUN apt-get install -y python3 python3-pip

RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev poppler-utils

ENV DEBIAN_FRONTEND=newt

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt

RUN python3 -m spacy download en_core_web_md

ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

CMD flask run --host=0.0.0.0