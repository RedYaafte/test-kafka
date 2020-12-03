import json
import requests

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

r = requests.get('http://localhost:3000/groups-opening')

openings = json.loads(r.text)

for opening in openings:
    key1 = opening.get('key1', None)
    if key1:
        producer.send('openings', {'key1': key1})
        producer.flush()
    print(key1)


print('====>  END  <====')
