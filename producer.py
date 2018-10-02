import os
import logging

from confluent_kafka import Producer


logging.basicConfig(level=logging.DEBUG)


conf = {
    'bootstrap.servers': os.environ['CLOUDKARAFKA_BROKERS'],
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'ssl.ca.location': './cloudkarafka.ca',
    'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
    'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD'],
}


p = Producer(**conf)
p.produce(os.environ['CLOUDKARAFKA_TOPIC'], '')
p.flush()
