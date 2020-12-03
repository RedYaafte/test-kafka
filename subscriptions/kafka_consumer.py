import os
import json

from kafka import KafkaConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

import django
django.setup()

from subscriptions.models import Group, Subscription


consumer = KafkaConsumer('quickstart-events')


for msg in consumer:
    try:
        value = json.loads(msg.value.decode('utf-8'))
    except:
        print(msg.value)
        pass

    if type(value) is dict:
        mnemonic = value.get('mnemonic')
        email = value.get('email')
        group = Group.objects.get(mnemonic=mnemonic)
        subscription = Subscription.objects.create(
            group=group, user=email)
        print(f'id:{subscription.id}, user: {subscription.user}')
