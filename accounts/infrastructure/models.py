from django.db import models
from django.contrib.auth.models import AbstractUser

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Dono do Salão'),
        ('staff', 'Profissional/Staff'),
        ('client', 'Cliente'),
    )
    
    # Cada usuário pertence a um Tenant (multi-tenant)
    # Null=True para permitir superusuários globais se necessário, mas em geral obrigatório.
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE, 
        related_name='users',
        null=True,
        blank=True
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    # Altera os grupos e permissões para evitar conflitos de nomes se necessário
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Os grupos a que este usuário pertence.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Permissões específicas para este usuário.'
    )

    def __str__(self):
        return f"{self.email} ({self.role})"
