# Generated by Django 3.1.3 on 2020-12-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
