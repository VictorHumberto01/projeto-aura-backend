import datetime
from .entities import Tenant
from .repositories import TenantRepositoryInterface

class TenantDomainService:
    def __init__(self, tenant_repo: TenantRepositoryInterface):
        self.tenant_repo = tenant_repo

    def register_new_salon(self, name: str, subdomain: str) -> Tenant:
        """
        Regra de negócio para criar um novo salão (tenant).
        Valida se o subdomínio já existe.
        """
        existing = self.tenant_repo.get_by_subdomain(subdomain)
        if existing:
            raise ValueError(f"O subdomínio '{subdomain}' já está em uso por outro salão.")

        new_tenant = Tenant(
            id=None,
            name=name,
            subdomain=subdomain.lower().strip(),
            created_at=datetime.datetime.now(),
            is_active=True
        )

        return self.tenant_repo.save(new_tenant)
