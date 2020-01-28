from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)


class UserProfile(models.Model):
    balance = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Transaction(models.Model):
    who = models.CharField(max_length=100)
    whom = models.CharField(max_length=100)
    how = models.CharField(max_length=100)
