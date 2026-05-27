from rest_framework import serializers

class TenantRegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True, help_text="Nome do Salão/Negócio")
    subdomain = serializers.CharField(max_length=100, required=True, help_text="Subdomínio único para o salão")

    def validate_subdomain(self, value):
        import re
        value = value.lower().strip()
        if not re.match(r'^[a-z0-9\-]+$', value):
            raise serializers.ValidationError(
                "O subdomínio deve conter apenas letras minúsculas, números e hífens."
            )
        return value
