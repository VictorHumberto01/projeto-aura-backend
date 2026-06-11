### [BACK-002] Autenticação via JWT e Controle de Papéis (RBAC)
**Dependências:** [BACK-001]

**Objetivo:** Implementar o sistema de login utilizando JSON Web Tokens e definir os papéis de acesso: Dono do Salão, Profissional/Staff e Cliente.

**Como Fazer:** 
1. Instalar e configurar a lib `djangorestframework-simplejwt`.
2. Criar um modelo Custom User (`CustomUser`) herdando de `AbstractUser` e adicionar um campo `role` (choices: OWNER, PROFESSIONAL, CLIENT).
3. Criar os endpoints de registro, login, refresh de token e perfil do usuário.
4. Criar classes de permissão do DRF customizadas (ex: `IsOwner`, `IsProfessional`, `IsClient`) para proteger as rotas adequadamente.

**Arquitetura da Tarefa:**
- App: `accounts` ou `users`
- Models: `CustomUser`
- Endpoints: `/api/auth/login/`, `/api/auth/register/`, `/api/auth/refresh/`, `/api/auth/me/`
- DRF Permissions: `IsOwner`, `IsProfessional`, `IsClient`

**DoD:**
- Um usuário consegue se cadastrar, fazer login e receber um token JWT válido.
- Rotas restritas retornam `401 Unauthorized` se acessadas sem token.
- Um "Cliente" recebe `403 Forbidden` ao tentar acessar rotas protegidas pelo papel de "Dono do Salão".
