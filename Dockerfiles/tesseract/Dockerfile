FROM ubuntu:20.04
LABEL author="akempler@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

#RUN add-apt-repository universe

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-add-repository universe
RUN apt-get install -y python3 python3-pip
# NOTE this gives me Python 3.6.11 ????

#RUN apt-get install -y python3-pip python3-dev build-essential
#RUN apt-get update && apt install -y libsm6 libxext6
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev

ENV DEBIAN_FRONTEND=newt

WORKDIR /app

COPY requirements.txt ./requirements.txt
#WORKDIR /app
#RUN pip install pillow
#RUN pip install flask
# RUN apt-get install python3-imaging # https://github.com/madmaze/pytesseract
#RUN pip install pytesseract
# RUN pip install opencv-contrib-python
# RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]
#CMD ["python", "app.py"]
#RUN ls -l

RUN pip3 install -r ./requirements.txt

CMD ["python3", "app.py"]
#CMD ["python3", "/app/app.py"]