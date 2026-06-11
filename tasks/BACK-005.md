### [BACK-005] Horário de Funcionamento e Jornada de Trabalho
**Dependências:** [BACK-003]

**Objetivo:** Definir os dias e horários em que o salão opera e qual a jornada de trabalho individual de cada profissional.

**Como Fazer:** 
1. Criar modelo `SalonBusinessHour` (dia da semana, hora de abertura, hora de fechamento).
2. Criar modelo `ProfessionalAvailability` (dia da semana, hora início, hora fim, vinculado ao profissional).
3. Implementar validações (clean/save) para garantir que a disponibilidade do profissional não exceda o horário do salão.

**Arquitetura da Tarefa:**
- App: `scheduling`
- Models: `SalonBusinessHour`, `ProfessionalAvailability`
- Endpoints: `/api/salon/hours/`, `/api/professionals/<id>/hours/`

**DoD:**
- Gestor consegue salvar o quadro de horários do salão.
- Profissional/Gestor conseguem salvar a grade horária do profissional.
- Conflitos e horários ilógicos (ex: fim antes do início) são rejeitados na API (HTTP 400).
