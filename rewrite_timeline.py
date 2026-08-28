import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<h2>Veja o seu site ganhando vida.</h2>',
    '<h2>Seu site em poucos passos.</h2>',
    html
)

html = re.sub(
    r'<p>Processo ultraotimizado.*?dias.</p>',
    '',
    html, flags=re.DOTALL
)

steps = """
            <div class="timeline-connected-grid reveal delay-1" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px;">
                <div class="timeline-step-card has-spotlight reveal">
                    <div class="step-header-row">
                        <span class="step-number">01</span>
                    </div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 8px;">Você fala com a gente</h3>
                    <p style="font-size: 0.9rem;">Envie as informações do seu negócio pelo WhatsApp.</p>
                </div>

                <div class="timeline-step-card has-spotlight reveal delay-1">
                    <div class="step-header-row">
                        <span class="step-number">02</span>
                    </div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 8px;">Nós criamos</h3>
                    <p style="font-size: 0.9rem;">Montamos o site com base no seu negócio e no segmento escolhido.</p>
                </div>

                <div class="timeline-step-card has-spotlight reveal delay-2">
                    <div class="step-header-row">
                        <span class="step-number">03</span>
                    </div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 8px;">Você aprova</h3>
                    <p style="font-size: 0.9rem;">Você visualiza o resultado e aprova o design antes de pagar o setup.</p>
                </div>

                <div class="timeline-step-card has-spotlight reveal delay-3">
                    <div class="step-header-row">
                        <span class="step-number">04</span>
                    </div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 8px;">Publicamos</h3>
                    <p style="font-size: 0.9rem;">Seu site vai para o ar e fica pronto para seus clientes acessarem.</p>
                </div>

                <div class="timeline-step-card has-spotlight reveal delay-4">
                    <div class="step-header-row">
                        <span class="step-number">05</span>
                    </div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 8px;">Nós cuidamos</h3>
                    <p style="font-size: 0.9rem;">Hospedagem, manutenção e suporte ficam por nossa conta.</p>
                </div>
            </div>
"""

html = re.sub(
    r'<div class="timeline-connected-grid reveal delay-1">.*?</div>\s*</div>\s*</section>',
    steps + '</div>\n      </section>',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
