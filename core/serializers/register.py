from rest_framework import serializers
from custom_auth.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'password', 'is_student', 'is_teacher', 'group', 'is_staff')

    def create(self, validated_data):
        password = validated_data.pop('password')
        is_staff = validated_data.pop('is_staff', True)
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.is_staff = is_staff
        user.save()
        return user
