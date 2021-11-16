FROM python:3.9.1
ADD . /calc2
WORKDIR /calc2
RUN pip install -r requirements.txt