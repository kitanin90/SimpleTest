from .models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'balance', 'currency', 'password')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'who', 'whom', 'how')
