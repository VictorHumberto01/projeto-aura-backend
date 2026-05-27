from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from ..domain.services import TenantDomainService
from ..infrastructure.repositories import DjangoTenantRepository
from .serializers import TenantRegisterSerializer

class TenantRegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Registrar novo Salão (Tenant)",
        description="Endpoint para registrar um novo salão no ecossistema Aura sob um subdomínio exclusivo.",
        request=TenantRegisterSerializer,
        responses={
            201: dict(description="Salão criado com sucesso"),
            400: dict(description="Erro de validação ou subdomínio duplicado")
        }
    )
    def post(self, request):
        serializer = TenantRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        
        # Injeção de dependências: Passa o repositório concreto da infraestrutura para o serviço de domínio.
        tenant_repo = DjangoTenantRepository()
        domain_service = TenantDomainService(tenant_repo)

        try:
            new_tenant = domain_service.register_new_salon(
                name=validated_data['name'],
                subdomain=validated_data['subdomain']
            )
            return Response({
                "id": new_tenant.id,
                "name": new_tenant.name,
                "subdomain": new_tenant.subdomain,
                "created_at": new_tenant.created_at.isoformat(),
                "is_active": new_tenant.is_active,
                "message": "Salão registrado com sucesso no ecossistema Aura."
            }, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
