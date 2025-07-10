from django.db import models
from custom_auth.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    departments = models.ManyToManyField(Department, related_name='teachers')
    courses = models.ManyToManyField(Course, related_name='teachers')
    description = models.TextField()

    def __str__(self):
        return f"{self.teacher.username} ({self.teacher.phone_number})"
