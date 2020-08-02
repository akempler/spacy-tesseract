FROM ubuntu:20.04
LABEL author="akempler@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-add-repository universe
RUN apt-get install -y python3 python3-pip

RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev

ENV DEBIAN_FRONTEND=newt

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt

CMD ["python3", "app.py"]
