from django.db import models

from core.models.student import Student


class Payment(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    def __str__(self):
        return f"{self.student.phone_number} - {self.amount} - {self.status}"
