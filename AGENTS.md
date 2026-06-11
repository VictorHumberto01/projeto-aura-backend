<!-- BEGIN:aura-project-rules -->
# Aura Project Architecture
- Project: Multi-Tenant SaaS for beauty salons.
- Monorepo: Backend in `/projeto-aura-backend` (Django DDD), Frontend in `/projeto-aura-frontend` (Next.js).
- Orchestration: Root `docker-compose.yml` (`docker-compose up --build`).
<!-- END:aura-project-rules -->

<!-- BEGIN:backend-ddd-rules -->
# Backend: Django + Domain-Driven Design (DDD)
- NEVER use default `views.py` or `models.py` in the root of an app.
- Directory Structure per App:
  - `/api/`: `views.py` (DRF Views), `serializers.py`, `urls.py`. HTTP interactions ONLY.
  - `/domain/`: `services.py`, `entities.py`. Pure business logic, no Django ORM if possible.
  - `/infrastructure/`: `models.py` (Django ORM), `repositories.py` (Data Access).
- MULTI-TENANT ISOLATION: ALL domain models (`Service`, `Appointment`, `Product`) MUST have a foreign key to `Tenant`. NEVER return or mutate global data without filtering by the current tenant.
- TASKS: Backend tasks are documented in `/projeto-aura-backend/tasks/`. ALWAYS read the respective `BACK-*.md` file before coding.
<!-- END:backend-ddd-rules -->

<!-- BEGIN:frontend-vibecoding-rules -->
# Frontend: Next.js + Tailwind CSS
- VIBECODING: Frontend is agile and dynamic. No strict tasks.
- AESTHETICS: Focus on premium design and dynamic UX. NEVER use generic browser colors (plain red, blue). Use sophisticated palettes (HSL, dark themes, glassmorphism) and modern typography (Google Fonts).
- INTERACTIVITY: Add micro-animations, hover effects, and state transitions. The interface must feel alive.
- STYLING: Maximize Tailwind CSS capabilities.
<!-- END:frontend-vibecoding-rules -->

<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:agent-behavior-rules -->
# Agent Behavior Guidelines
- DO NOT break the DDD structure. Create directories ONLY if strictly required for the business domain.
- DO NOT use shell commands for file operations (cat/grep). Use native environment tools (`read_file`, `write_to_file`, `grep_search`).
- ALWAYS communicate implementation plans before executing backend tasks.
- IF DDD rules conflict with Django conventions, stop and ask the user for the best tactical adaptation.
<!-- END:agent-behavior-rules -->
