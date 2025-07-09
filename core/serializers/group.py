from rest_framework import serializers
from core.models.group import GroupStudent
from core.models.payment import Payment


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = ['id', 'title', 'description', 'course', 'teacher', 'start_date', 'end_date']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'student', 'amount', 'date', 'status']
