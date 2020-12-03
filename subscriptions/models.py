from django.db import models


class Group(models.Model):

    mnemonic = models.CharField(max_length=100)
    course = models.PositiveIntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    schedule = models.PositiveIntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mnemonic


class Subscription(models.Model):

    group = models.ForeignKey(
        Group, related_name='subscriptions', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user