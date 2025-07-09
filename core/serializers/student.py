from core.serializers.user import UserSerializer
from core.models.student import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        groups = validated_data.pop('group', [])

        user = UserSerializer().create(user_data)
        student = Student.objects.create(user=user, **validated_data)

        student.group.set(groups)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data('user', None)

        if user_data:
            UserSerializer().update(instance.user, user_data)

        for key, value in validated_data.items():
            field = instance._mete.get_field(key)
            if field.many_to_many:
                getattr(instance, key).set(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
