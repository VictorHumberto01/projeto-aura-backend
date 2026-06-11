### [BACK-007] Controle de Estoque de Produtos
**Dependências:** [BACK-001]

**Objetivo:** Gerenciar a entrada, consumo e inventário físico de produtos e materiais do salão.

**Como Fazer:** 
1. Criar o modelo `Product` (Nome, SKU, Quantidade atual, Quantidade mínima para alerta).
2. Criar o modelo `StockTransaction` (Tipo: Entrada/Saída, Quantidade movimentada, Justificativa, Data).
3. Utilizar signals ou lógica na API (no `perform_create` da transação) para atualizar a "Quantidade atual" do produto correspondente automaticamente ao registrar uma transação.
4. Construir os endpoints.

**Arquitetura da Tarefa:**
- App: `inventory`
- Models: `Product`, `StockTransaction`
- Endpoints: `/api/inventory/products/`, `/api/inventory/transactions/`

**DoD:**
- CRUD de produtos está funcional.
- Nova transação de "Entrada" aumenta o estoque; "Saída" diminui o estoque.
- Requisições para criar "Saída" maior do que o estoque existente são rejeitadas.
