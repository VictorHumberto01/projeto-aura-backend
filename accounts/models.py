from .infrastructure.models import Tenant, User

# Expondo os modelos ORM para descoberta automática do Django e geração de migrações.
__all__ = ['Tenant', 'User']
