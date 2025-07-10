from django.db import models

from core.models.group import GroupStudent
from custom_auth.models import CustomUser


class Attendance(models.Model):
    STATUS = (

        ('present', 'Keldi'),
        ('late', 'Kechikdi'),
        ('absent', 'Kelmadi'),
    )
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='absent')

    class Meta:
        unique_together = ('student', 'group', 'date')
        verbose_name = 'Davomat'
        verbose_name_plural = 'Davomatlar'

    def __str__(self):
        return f"{self.student.phone_number} - {self.group.title} - {self.date} - {self.get_status_display()}"
