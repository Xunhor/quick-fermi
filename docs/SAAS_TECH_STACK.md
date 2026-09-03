# Visão de Arquitetura e Tech Stack (Futuro SaaS)

Este documento registra a stack tecnológica recomendada para quando o projeto **Boomo** evoluir de Landing Pages estáticas para uma **Plataforma de Software como Serviço (SaaS)**.

## Por que essa Stack?
Como um assistente de inteligência artificial de ponta, eu leio e escrevo código em dezenas de linguagens. No entanto, a stack abaixo é a **"Stack de Ouro"** para colaboração humano-IA. Ela maximiza a velocidade de desenvolvimento, minimiza bugs e garante escalabilidade.

---

### 1. Frontend & Framework: Next.js + React
- **Papel:** Criação das interfaces (Painel do Cliente, Dashboard, Construtor).
- **Por que é ideal para IA:** O Next.js possui regras de arquitetura muito claras. Ele permite que eu crie páginas inteiras sabendo exatamente onde colocar cada arquivo, garantindo SEO e alta performance.

### 2. Estilização: Tailwind CSS
- **Papel:** Design de interfaces, Dark Mode e responsividade.
- **Por que é ideal para IA:** Permite estilizar componentes diretamente no código. Posso construir interfaces premium (padrão Vercel/Apple) instantaneamente sem precisar gerenciar inúmeros arquivos .css.

### 3. Linguagem de Programação: TypeScript
- **Papel:** Tipagem estática estrutural.
- **Por que é ideal para IA:** A peça mais importante. O TypeScript define regras rígidas. Isso impede lucinações de IA e evita a quebra de dados invisíveis. O código auto-valida minha lógica antes de ir pro ar.

### 4. Backend & Autenticação: Supabase (PostgreSQL)
- **Papel:** Banco de dados de clientes, logins, pagamentos, assinaturas e hospedagem das variáveis dos sites.
- **Por que é ideal para IA:** Backend-as-a-service. Eu não preciso perder dias construindo APIs de login do zero; conectamos o Supabase e eu foco em construir as regras de negócio de alto valor para a Boomo.

---

## Roadmap de Arquitetura

1. **Fase Atual:** HTML/CSS/JS puros. Ideal para validação, vendas diretas, extrema velocidade de carregamento e hospedagem 100% gratuita (ex: GitHub Pages).
2. **Fase Futura (SaaS):** Migração do painel de operações e criação da área do cliente utilizando Next.js + Supabase, conectando-se diretamente com o Abacate Pay para automatizar as cobranças mensais das clínicas e escritórios.
