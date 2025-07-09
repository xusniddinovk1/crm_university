from rest_framework import serializers
from core.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment  # Model nomi
        fields = ['id', 'student', 'amount', 'date', 'status']
