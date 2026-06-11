### [BACK-006] Motor de Agendamento e Gestão de Exceções (Bloqueios)
**Dependências:** [BACK-004], [BACK-005]

**Objetivo:** Responsável pelo core do negócio: agendar horários, bloquear períodos (folgas/feriados) e calcular dinamicamente a disponibilidade de agenda.

**Como Fazer:** 
1. Criar o modelo `Appointment` (Relacionando Cliente, Profissional, Serviço, Data/Hora Início, Data/Hora Fim, Status).
2. Criar o modelo `TimeBlock` (Bloqueios manuais com data/hora de início e fim e motivo).
3. Criar uma classe Service (`AvailabilityService`) contendo a lógica pesada de cálculo:
   - Dado um Dia + Profissional + Duração do Serviço:
   - Buscar a jornada padrão (`ProfessionalAvailability`).
   - Subtrair os períodos contidos em `TimeBlock`.
   - Subtrair os horários já ocupados em `Appointment`.
   - Retornar os slots livres em intervalos.
4. Criar endpoint `/api/availability/` para ser consumido pelo frontend e endpoint `/api/appointments/` para efetivação do agendamento.

**Arquitetura da Tarefa:**
- App: `appointments`
- Models: `Appointment`, `TimeBlock`
- Services: `AvailabilityService` (Python puro)
- Endpoints: `/api/appointments/`, `/api/availability/`, `/api/blocks/`

**DoD:**
- Agendamentos podem ser criados, confirmados, cancelados ou concluídos.
- Endpoint de disponibilidade retorna corretamente horários livres (testado com bloqueios e múltiplos serviços no mesmo dia).
- O sistema impede a criação de um agendamento em horário não disponível ou que já passou.
