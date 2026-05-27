from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import Tenant, User

class TenantRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, tenant_id: int) -> Optional[Tenant]:
        pass

    @abstractmethod
    def get_by_subdomain(self, subdomain: str) -> Optional[Tenant]:
        pass

    @abstractmethod
    def save(self, tenant: Tenant) -> Tenant:
        pass


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
