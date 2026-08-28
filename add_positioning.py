import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

posicionamento = """
    <!-- 4. NOVA MENSAGEM DE POSICIONAMENTO -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
        <div class="container text-center reveal">
            <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 24px;">Um site profissional sem a complicação de uma agência.</h2>
            <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 650px; margin: 0 auto; line-height: 1.6;">
                A Boomo transforma a criação e manutenção do seu site em uma assinatura simples.<br><br>
                Sem projetos demorados, orçamentos complexos ou preocupação com hospedagem e manutenção.<br>
                <strong style="color: var(--text-main); font-weight: 600;">Você envia as informações. Nós cuidamos do resto.</strong>
            </p>
        </div>
    </section>
"""

html = html.replace('<!-- 4. COMO FUNCIONA (Timeline) -->', posicionamento + '\n    <!-- 4. COMO FUNCIONA (Timeline) -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
