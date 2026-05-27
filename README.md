# Aura - Backend (Django REST Framework)

Este repositório contém o backend do **Projeto Aura**, uma plataforma SaaS focada na gestão e agendamento para profissionais e salões de beleza. A aplicação é construída com Python e Django, utilizando Django REST Framework (DRF) para expor as APIs consumidas pelo frontend.

---

## 🚀 Como Executar o Servidor

O projeto está totalmente configurado para rodar utilizando **Docker** e **Docker Compose**, o que simplifica a inicialização do banco de dados PostgreSQL e do servidor de desenvolvimento.

### Pré-requisitos
- Docker instalado em sua máquina.
- Docker Compose instalado.

### Executando com Docker Compose

1. **Configurar Variáveis de Ambiente:**
   O projeto vem com um arquivo de exemplo `.env.example`. Copie-o para criar o `.env` de desenvolvimento:
   ```bash
   cp .env.example .env
   ```
   *(Os valores padrão já estão configurados para funcionar perfeitamente com o Docker Compose local).*

2. **Iniciar os Serviços:**
   Execute o comando abaixo na raiz deste repositório para construir e iniciar os containers do banco de dados e do servidor:
   ```bash
   docker compose up --build
   ```
   *Este comando irá:*
   - Baixar e configurar a imagem do PostgreSQL.
   - Construir o container Django e instalar as dependências.
   - Executar automaticamente as migrações do banco de dados (`python manage.py migrate`).
   - Iniciar o servidor de desenvolvimento com hot-reload ativo.

3. **Verificar se os Containers estão Saudáveis:**
   O container do Django possui um Healthcheck acoplado que monitora o endpoint `/api/health/`. Você pode ver o status dos containers usando:
   ```bash
   docker compose ps
   ```

4. **Acessar a Aplicação:**
   - Servidor Django: [http://localhost:8000](http://localhost:8000)
   - Endpoint de Healthcheck: [http://localhost:8000/api/health/](http://localhost:8000/api/health/)

---

## 📖 Documentação da API (Swagger/OpenAPI)

O backend possui autogeração de documentação OpenAPI 3.0 através do pacote `drf-spectacular`.

Quando o servidor estiver rodando, você pode acessar:
- **Swagger UI:** [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/) (Interface interativa para testar as rotas).
- **ReDoc:** [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/) (Layout alternativo e limpo de leitura).
- **Esquema JSON/YAML bruto:** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---

## 🛠️ Diretrizes de Desenvolvimento e Arquitetura

Para garantir consistência, manutenibilidade e a segurança das informações das clientes e salões, todo o código do servidor deve seguir os seguintes padrões:

### 1. Padrão de Estrutura de Apps Django
Evite criar uma única aplicação gigante. Divida o sistema em apps modulares usando `python manage.py startapp <nome_app>`. Por exemplo:
- `accounts`: Contas de salões/empresas (Tenants) e autenticação de usuários.
- `services`: CRUD de serviços de beleza, preços, durações e especialidades.
- `staff`: Cadastro de profissionais de equipe, jornadas de trabalho e disponibilidades.
- `bookings`: Motor de agendamento e cálculo de horários disponíveis.
- `inventory`: Controle de estoque de materiais e produtos.

### 2. Multi-Tenancy (Isolamento de Dados desde o Dia 1)
> [!IMPORTANT]
> **Esta é a regra mais crítica do backend:** A plataforma é um SaaS multi-tenant. Dados de um salão/profissional nunca podem vazar para outro.
- **Modelo Base:** Todas as tabelas que guardam dados específicos de negócios (como profissionais, serviços, produtos, agendamentos, clientes) devem obrigatoriamente possuir uma chave estrangeira para o modelo que representa a conta do salão (ex: `Account` ou `Tenant`).
  ```python
  class TenantModel(models.Model):
      tenant = models.ForeignKey('accounts.Tenant', on_delete=models.CASCADE)
      
      class Meta:
          abstract = True
  ```
- **QuerySets customizados:** Para evitar esquecimentos nas consultas, crie um `Manager` ou use um middleware que filtre automaticamente todas as queries do banco pelo ID do tenant logado na requisição (por exemplo, extraído do token do usuário).

### 3. Autenticação e Autorização
- **Autenticação:** Baseada em JSON Web Tokens (JWT) utilizando `djangorestframework-simplejwt`.
- **Níveis de Acesso (RBAC):** Os usuários pertencem a papéis bem definidos:
  - **Dono do Salão (Tenant Admin):** Acesso total aos dados de faturamento, equipe, serviços e configurações.
  - **Profissional/Staff:** Acesso para visualizar e gerenciar sua própria agenda e dados básicos do perfil.
  - **Cliente:** Acesso limitado ao portal público de agendamentos.
- Sempre decore suas views com a classe de permissão apropriada do DRF (ex: `@permission_classes([IsAuthenticated])`).

### 4. Boas Práticas do Django REST Framework (DRF)
- **Serializers:** Use serializers para validação rigorosa de dados de entrada e saída. Não faça lógica de validação complexa dentro de views.
- **Class-Based Views (CBVs):** Prefira usar `ModelViewSet` ou views genéricas do DRF (`ListAPIView`, `CreateAPIView`, etc.) pois elas integram nativamente com o gerador do Swagger e reduzem a escrita de código boilerplate.
- **Documentação de Rotas:** Ao criar novos endpoints, utilize os decorators do `drf-spectacular` (como `@extend_schema`) para documentar parâmetros de query, cabeçalhos ou formatos de resposta customizados.

---

## 🛠️ Desenvolvimento Sem Docker (Local)

Se desejar executar o backend diretamente na sua máquina física:

1. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as credenciais no `.env`** apontando para o seu banco de dados local.

4. **Execute as migrações e rode o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
