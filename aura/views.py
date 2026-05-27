from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Health Check",
    description="Endpoint para checar a integridade/saúde do servidor e conexões do sistema.",
    responses={200: dict}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Retorna o status de saúde da aplicação.
    Útil para monitoramento do docker-compose e deploys.
    """
    return Response({
        "status": "healthy",
        "message": "Servidor Aura está operacional."
    }, status=200)
