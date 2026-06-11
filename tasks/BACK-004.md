### [BACK-004] Catálogo de Serviços e Especialidades
**Dependências:** [BACK-001], [BACK-003]

**Objetivo:** Criar e gerenciar os serviços oferecidos pelo salão, bem como vincular quais profissionais estão aptos a realizar cada serviço.

**Como Fazer:** 
1. Criar o modelo `Service` (Nome, descrição, duração estimada em minutos, preço padrão).
2. Criar relacionamento (ManyToMany) para associar um `ProfessionalProfile` a múltiplos `Service`. 
3. Desenvolver os serializers e endpoints de CRUD para os serviços.
4. Criar rotas para atribuir/desatribuir serviços a um profissional específico.

**Arquitetura da Tarefa:**
- App: `services` ou `catalog`
- Models: `Service`
- Endpoints: `/api/services/`, `/api/professionals/<id>/services/`

**DoD:**
- Endpoints de listagem, criação, edição e exclusão de serviços operacionais.
- É possível obter a lista de serviços que um profissional X realiza.
- É possível obter a lista de profissionais que realizam um serviço Y.
