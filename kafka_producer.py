import json

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send(
    'quickstart-events',
    {'mnemonic': 'LALALA01', 'email': 'student@student.org'})
producer.flush()
print('END')
