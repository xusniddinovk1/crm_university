from rest_framework import serializers


class AttendanceSerializer(serializers.ModelSerializer):
    STATUS = (
        ('present', 'Keldi'),
        ('late', 'Kechikdi'),
        ('absent', 'Kelmadi')
    )
    student_id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=STATUS)


class GroupAttendanceGETResponseSerializer(serializers.Serializer):
    attendance_data = AttendanceSerializer(many=True)
