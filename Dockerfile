FROM python:3.6-slim

RUN apt-get -y update
RUN apt-get -y install wget apt-transport-https gnupg2 software-properties-common

RUN wget -qO - https://packages.confluent.io/deb/5.0/archive.key | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.0 stable main"
RUN apt-get -y install librdkafka1


WORKDIR /app
ADD producer.py /app/
RUN wget https://www.cloudkarafka.com/certs/cloudkarafka.ca

RUN pip install confluent-kafka

CMD ["python", "producer.py"]
