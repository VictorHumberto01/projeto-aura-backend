from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Tenant:
    id: Optional[int]
    name: str
    subdomain: str
    created_at: datetime.datetime
    is_active: bool = True

    def deactivate(self):
        """Domain logic to deactivate a tenant."""
        self.is_active = False

    def activate(self):
        """Domain logic to activate a tenant."""
        self.is_active = True


@dataclass
class User:
    id: Optional[int]
    email: str
    name: str
    role: str  # 'owner', 'staff', 'client'
    tenant_id: int
    is_active: bool = True
