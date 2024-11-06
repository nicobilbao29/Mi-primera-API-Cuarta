from rest_framework import serializers
from .models import User # Asegúrate de que el nombre sea correcto

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Asegúrate de usar el modelo correcto
        fields = '__all__'   # Incluye los campos que deseas serializar
