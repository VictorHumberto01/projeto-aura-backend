### [BACK-003] Gestão de Perfis (Salão, Profissionais e Clientes)
**Dependências:** [BACK-001], [BACK-002]

**Objetivo:** Permitir a configuração das informações públicas e administrativas do salão, além de associar e gerenciar a equipe (profissionais) e as clientes.

**Como Fazer:** 
1. Criar `SalonProfile` vinculado ao Tenant, com campos para nome de exibição, logo, descrição e link público.
2. Criar `ProfessionalProfile` vinculado ao CustomUser (OneToOne) e ao Tenant (ForeignKey), contendo bio e foto.
3. Criar `ClientProfile` vinculado ao CustomUser e ao Tenant, contendo histórico e anotações.
4. Construir APIs CRUD para gerenciar essas entidades.

**Arquitetura da Tarefa:**
- App: `profiles`
- Models: `SalonProfile`, `ProfessionalProfile`, `ClientProfile`
- Endpoints: `/api/salon/profile/`, `/api/professionals/`, `/api/clients/`

**DoD:**
- O Dono consegue atualizar os dados do salão.
- O Dono consegue cadastrar/convidar e listar membros da equipe.
- O Profissional consegue editar a própria biografia.
- Dados vazados para o Frontend possuem as devidas restrições baseadas no Tenant.
