from typing import Optional
from django.utils import timezone
from ..domain.entities import Tenant as DomainTenant, User as DomainUser
from ..domain.repositories import TenantRepositoryInterface, UserRepositoryInterface
from .models import Tenant as TenantORM, User as UserORM

class DjangoTenantRepository(TenantRepositoryInterface):
    def _to_domain(self, orm_tenant: TenantORM) -> DomainTenant:
        return DomainTenant(
            id=orm_tenant.id,
            name=orm_tenant.name,
            subdomain=orm_tenant.subdomain,
            created_at=orm_tenant.created_at,
            is_active=orm_tenant.is_active
        )

    def get_by_id(self, tenant_id: int) -> Optional[DomainTenant]:
        try:
            orm_tenant = TenantORM.objects.get(id=tenant_id)
            return self._to_domain(orm_tenant)
        except TenantORM.DoesNotExist:
            return None

    def get_by_subdomain(self, subdomain: str) -> Optional[DomainTenant]:
        try:
            orm_tenant = TenantORM.objects.get(subdomain=subdomain.lower().strip())
            return self._to_domain(orm_tenant)
        except TenantORM.DoesNotExist:
            return None

    def save(self, tenant: DomainTenant) -> DomainTenant:
        if tenant.id:
            # Update
            orm_tenant = TenantORM.objects.get(id=tenant.id)
            orm_tenant.name = tenant.name
            orm_tenant.subdomain = tenant.subdomain
            orm_tenant.is_active = tenant.is_active
            orm_tenant.save()
        else:
            # Create
            orm_tenant = TenantORM.objects.create(
                name=tenant.name,
                subdomain=tenant.subdomain,
                is_active=tenant.is_active
            )
            tenant.id = orm_tenant.id
            tenant.created_at = orm_tenant.created_at
        return tenant


class DjangoUserRepository(UserRepositoryInterface):
    def _to_domain(self, orm_user: UserORM) -> DomainUser:
        return DomainUser(
            id=orm_user.id,
            email=orm_user.email,
            name=orm_user.first_name + " " + orm_user.last_name,
            role=orm_user.role,
            tenant_id=orm_user.tenant_id,
            is_active=orm_user.is_active
        )

    def get_by_id(self, user_id: int) -> Optional[DomainUser]:
        try:
            orm_user = UserORM.objects.get(id=user_id)
            return self._to_domain(orm_user)
        except UserORM.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Optional[DomainUser]:
        try:
            orm_user = UserORM.objects.get(email=email)
            return self._to_domain(orm_user)
        except UserORM.DoesNotExist:
            return None

    def save(self, user: DomainUser) -> DomainUser:
        first_name, *last_names = user.name.split(" ", 1)
        last_name = last_names[0] if last_names else ""
        
        if user.id:
            orm_user = UserORM.objects.get(id=user.id)
            orm_user.email = user.email
            orm_user.first_name = first_name
            orm_user.last_name = last_name
            orm_user.role = user.role
            orm_user.tenant_id = user.tenant_id
            orm_user.is_active = user.is_active
            orm_user.save()
        else:
            orm_user = UserORM.objects.create(
                username=user.email, # Django standard requires username
                email=user.email,
                first_name=first_name,
                last_name=last_name,
                role=user.role,
                tenant_id=user.tenant_id,
                is_active=user.is_active
            )
            user.id = orm_user.id
        return user
