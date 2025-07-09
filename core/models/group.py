from django.db import models
from core.models.teacher import Course, Teacher


class GroupStudent(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name='groups')
    teacher = models.ManyToManyField(Teacher, related_name="groups_taught")
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField('CustomUser', related_name='group_students', blank=True,
                                      limit_choices_to={'is_student': True})


class Lesson(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f"{self.subject} - {self.teacher.phone_number} - {self.date}"
