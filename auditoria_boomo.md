# Auditoria Completa — Boomo (Estado Atual)

Conforme a diretriz de **Preservar -> Melhorar -> Validar** e a **Regra 2 (Nunca reescrever componentes sem necessidade)**, realizei uma varredura completa da estrutura, HTML, CSS, assets e rotas do projeto atual da Boomo.

O objetivo é fornecer um diagnóstico exato, mapeando o que funciona, o que foi quebrado e qual o caminho seguro para as próximas implementações.

---

## A. Estado Atual (O que está funcionando corretamente)

1. **Estrutura e Arquitetura:**
   - O projeto é **100% estático (Vanilla HTML/CSS/JS)**. Sem frameworks pesados (React/Next), sem build steps, rodando direto na Vercel com roteamento por ercel.json (que usa cleanUrls: true e cache headers).
   - Isso garante performance máxima (Nota 100 no PageSpeed) e extrema facilidade de manutenção.

2. **Design System (Apple-like Premium):**
   - O site implementa um tema **claro/escuro** purista, inspirado em diretrizes da Apple e Vercel (Minimalismo, fundo preto #000000, superfícies #18181B, textos #F5F5F7 ou #86868B).
   - Tipografia baseada na Inter (sans) e Plus Jakarta Sans. Sem gradientes roxos neon ou exageros de IA.

3. **Rotas e Páginas Auxiliares:**
   - As rotas auxiliares (/sobre, /onboarding, /termos-privacidade, /sucesso) estão intactas no diretório raiz.
   - Os templates de clientes reais/demonstrativos estão isolados corretamente na pasta /templates/ (estetica, odontologia, advocacia, contabilidade), cada um com seu próprio HTML e CSS, não interferindo no global.

4. **Copywriting e Oferta Comercial (Refatoração Recente):**
   - A copy está perfeitamente alinhada com as Regras de Negócio (Regra 7, 10, 11 e 13).
   - Hero matador: *"Seu negócio merece um site profissional."*
   - Redução de Risco Isolada: *"Sem pagar no escuro."*
   - Planos e preços atualizados e mantidos conforme a Regra 12 (Essencial R, Profissional R, Premium R).
   - "Como Funciona" reformulado para 5 passos didáticos.

5. **Responsividade Base:**
   - A grid de Preços e o grid de Timeline ("Como Funciona") usam CSS Grid uto-fit e minmax, o que garante que empilhem perfeitamente no celular sem estourar a tela.

---

## B. Problemas Encontrados (Inconsistências e Quebras)

1. **Tokens de CSS Ausentes:**
   - Na seção "Early Adopters" (Seja um dos primeiros), o título utiliza a cor ar(--accent-cyan) inline. No entanto, o CSS atual do projeto usa ar(--brand-accent) (Azul Apple #2997FF) e não possui o token --accent-cyan mapeado no :root. O texto perdeu o destaque de cor.

2. **Links de Templates (Iframes "Em desenvolvimento"):**
   - No Carrossel de "Sites demonstrativos", os templates *Advocacia* e *Contabilidade* estão linkando para src="about:blank" ou marcados como "Em desenvolvimento" no HTML, não renderizando os mockups finais para o usuário, apesar dos assets existirem na pasta /templates/advocacia/.

3. **Descompasso de Arquivos CSS (onts.css vs Inline):**
   - O projeto possui vários scripts de "inlining" e backups gerados que sujaram a raiz do projeto. O CSS vital foi jogado inteiro dentro do <style> do index.html (com quase 3000 linhas), tornando a manutenção manual perigosa e suscetível a erros de Regex.

---

## C. Possíveis Regressões (O que foi afetado pelas últimas ações)

1. **Remoção Global do Scroll Reveal (.reveal):**
   - Para resolver o bug de "tela preta", a classe .reveal foi removida indiscriminadamente de todo o HTML. Embora isso garanta o carregamento instantâneo, o site perdeu a sofisticação da entrada suave dos elementos (fading in). A lógica JS do IntersectionObserver continuou no fim do arquivo, rodando em vazio.

2. **Ícones FontAwesome:**
   - Há uma tentativa no <head> de carregar o FontAwesome de forma assíncrona (onload="this.media='all'"), o que pode gerar Flash of Unstyled Text (FOUT) onde os ícones aparecem quadrados por alguns milissegundos antes de carregar.

---

## D. Riscos (O que pode quebrar sem cuidado)

1. **Tocar no Inlined CSS (<style>):**
   - Qualquer substituição automática no arquivo index.html que afete o bloco <style> pode destruir o design system inteiro. É imperativo não usar substituição baseada em Regex no corpo todo.

2. **Z-Index do Mouse Glow:**
   - O efeito global de luz acompanhando o mouse (html.dark-theme::before e ::after) tem z-index muito alto e will-change. Modificar as propriedades de pointer-events: none acidentalmente pode bloquear todos os cliques na página (como nos botões do WhatsApp).

3. **Atualização de Preços Sem Consentimento (Regra 12):**
   - Se os blocos HTML de preço precisarem ser editados para design, os valores em si (R, R de setup, etc.) podem ser sobreescritos inadvertidamente se copiarmos templates genéricos.

---

## E. Plano Recomendado (Sequência Segura)

Conforme a Regra 26 (Modo de Trabalho), recomendo a seguinte implementação cirúrgica:

**Fase 1: Limpeza e Consistência (Baixo Risco)**
- Restaurar a classe ar(--brand-accent) nos textos que tentam usar ar(--accent-cyan).
- Remover a chamada JavaScript inútil do IntersectionObserver que ficou para trás, poupando processamento no client-side.

**Fase 2: Refinamento do Carrossel (Médio Risco)**
- Corrigir os paths do Iframe para Advocacia e Contabilidade para que puxem as pastas reais criadas (/templates/advocacia/index.html).

**Fase 3: Devolver as Animações com Segurança Absoluta (Baixo Risco, Alto Impacto)**
- Em vez de esconder elementos com opacity: 0 logo no CSS (o que causou a tela preta), usar uma classe .js-enabled .reveal { opacity: 0 } ou injetar as animações estritamente via JavaScript, garantindo 100% que a regressão nunca mais aconteça.

**Fase 4: Limpeza do Repositório (Organização)**
- Remover arquivos .py gerados durante o processo e arquivos .backup que estão enchendo a raiz do projeto e podem ir para produção na Vercel acidentalmente.
