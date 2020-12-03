import os
import json

from kafka import KafkaConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

import django
django.setup()

from subscriptions.models import Group, Subscription


consumer = KafkaConsumer('openings')


for msg in consumer:
    try:
        value = json.loads(msg.value.decode('utf-8'))
    except:
        print(msg.value)
        pass

    if type(value) is dict:
        mnemonic = value.get('key1', None)
        if mnemonic:
            group = Group.objects.filter(mnemonic=mnemonic)
            if group:
                print(f'This group already exist {group}.')
            else:
                gp = Group.objects.create(mnemonic=mnemonic)
                print(f'New group create with mnemonic: {mnemonic} and id: {gp.id}')

