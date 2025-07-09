from rest_framework import viewsets

from custom_auth.models import CustomUser
from core.serializers.register import UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        is_staff = self.request.data.get('is_staff', False)  # Swagger'dan is_staff olish
        serializer.save(is_staff=is_staff)  # User yaratishda is_staff ni saqlaymiz
