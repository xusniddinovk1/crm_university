from django.db import models
from custom_auth.models import CustomUser


class Student(models.Model):
    STATUS = (
        ('ongoing', "O'qiyotgan"),
        ('graduated', "Bitirgan"),
    )
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    status = models.CharField(max_length=20, choices=STATUS, default='ongoing')
    group = models.ManyToManyField('core.GroupStudent', related_name='students_group')
    is_line = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.student.phone_number
