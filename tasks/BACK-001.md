# [BACK-001] Setup do Projeto Django e Isolamento Multi-Tenant

**Dependências:** Nenhuma

**Objetivo:** Configurar a base do projeto Django, DRF, banco de dados PostgreSQL e implementar a arquitetura multi-tenant (Tenant Isolation) para garantir que os dados de diferentes salões nunca se misturem.

**Como Fazer:** 
1. Inicializar o projeto Django e instalar dependências (DRF, psycopg2, corsheaders).
2. Configurar conexão com o PostgreSQL.
3. Criar o modelo `Tenant` (ou `SalonAccount`) para representar a conta principal do salão.
4. Implementar isolamento lógico: Criar um modelo base abstrato (ex: `TenantAwareModel`) que contenha a chave estrangeira para `Tenant` e sobrescreva os managers para sempre filtrar pelo tenant ativo da request.
5. Criar um middleware para identificar o Tenant da requisição atual (baseado no usuário logado ou subdomínio/cabeçalho).

**Arquitetura da Tarefa:**
- App: `core` ou `tenants`
- Models: `Tenant`, `TenantAwareModel` (Abstract)
- Middlewares: `TenantMiddleware`

**DoD:**
- Projeto Django executando localmente sem erros.
- Banco de dados PostgreSQL conectado e migrações rodando com sucesso.
- O modelo base multi-tenant exige a presença de um tenant para salvar registros.
