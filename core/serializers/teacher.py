from rest_framework import serializers
from core.models.teacher import Teacher, Course, Department
from core.serializers.user import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'title', 'description']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    departments = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        departments = validated_data.pop('departments', [])
        courses = validated_data('course', [])
        user = UserSerializer().create(user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        teacher.departments.set(departments)
        teacher.course.set(courses)
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        departments = validated_data.pop('departments', None)
        courses = validated_data.pop('course', None)

        if user_data:
            UserSerializer().update(instance.user, user_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if departments is not None:
            instance.departments.set(departments)
        if courses is not None:
            instance.course.set(courses)
        return instance
