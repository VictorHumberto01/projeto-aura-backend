### [BACK-008] Dashboard de Gestão, Relatórios e Integrações
**Dependências:** [BACK-006], [BACK-007]

**Objetivo:** Consolidar e expor métricas do negócio e feed da Home Page (informes e dicas).

**Como Fazer:** 
1. Criar ViewSets com métodos baseados em agregações (Aggregation/Annotation no ORM do Django) para calcular: faturamento diário/mensal, quantidade de serviços por profissional, e próximos clientes do dia.
2. Criar modelo `Announcement` para informes internos do salão.
3. Fazer requisições HTTP para uma API externa (a definir) que traga dicas de beleza, caso os informes estejam vazios, incluindo cache via Redis ou locmemcache do Django para evitar throttling da API externa.

**Arquitetura da Tarefa:**
- App: `dashboard`, `communication`
- Models: `Announcement`
- Endpoints: `/api/dashboard/summary/`, `/api/reports/revenue/`, `/api/feed/`

**DoD:**
- Dashboard retorna o número correto de consultas e a receita baseada nos serviços `Concluídos`.
- Relatório básico gerado adequadamente respeitando o intervalo de datas.
- Feed carrega informes do banco e integra dica de parceiro/externo.
