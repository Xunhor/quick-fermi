import io

body = """
    <!-- 4. POSICIONAMENTO -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
        <div class="container text-center reveal">
            <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 24px; font-family: 'Plus Jakarta Sans', sans-serif;">Um site profissional sem a complicação de uma agência.</h2>
            <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 650px; margin: 0 auto; line-height: 1.6;">
                A Boomo transforma a criação e manutenção do seu site em uma assinatura simples.<br><br>
                Sem projetos demorados, orçamentos complexos ou preocupação com hospedagem e manutenção.<br>
                <strong style="color: var(--text-main); font-weight: 600;">Você envia as informações. Nós cuidamos do resto.</strong>
            </p>
        </div>
    </section>

    <!-- 5. COMO FUNCIONA -->
    <section id="como-funciona" class="section-padding timeline-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Seu site em poucos passos.</h2>
            </div>

            <div class="timeline-connected-grid reveal delay-1" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px;">
                <div class="timeline-step-card has-spotlight reveal">
                    <div class="step-header-row"><span class="step-number">01</span></div>
                    <h3 style="font-size: 1.1rem;">Você fala com a gente</h3>
                    <p style="font-size: 0.9rem; margin-top:8px;">Envie as informações do seu negócio pelo WhatsApp.</p>
                </div>
                <div class="timeline-step-card has-spotlight reveal delay-1">
                    <div class="step-header-row"><span class="step-number">02</span></div>
                    <h3 style="font-size: 1.1rem;">Nós criamos</h3>
                    <p style="font-size: 0.9rem; margin-top:8px;">Montamos o site com base no seu negócio e no segmento escolhido.</p>
                </div>
                <div class="timeline-step-card has-spotlight reveal delay-2">
                    <div class="step-header-row"><span class="step-number">03</span></div>
                    <h3 style="font-size: 1.1rem;">Você aprova</h3>
                    <p style="font-size: 0.9rem; margin-top:8px;">Você visualiza o resultado e aprova o design antes de pagar o setup.</p>
                </div>
                <div class="timeline-step-card has-spotlight reveal delay-3">
                    <div class="step-header-row"><span class="step-number">04</span></div>
                    <h3 style="font-size: 1.1rem;">Publicamos</h3>
                    <p style="font-size: 0.9rem; margin-top:8px;">Seu site vai para o ar e fica pronto para seus clientes acessarem.</p>
                </div>
                <div class="timeline-step-card has-spotlight reveal delay-4">
                    <div class="step-header-row"><span class="step-number">05</span></div>
                    <h3 style="font-size: 1.1rem;">Nós cuidamos</h3>
                    <p style="font-size: 0.9rem; margin-top:8px;">Hospedagem, manutenção e suporte ficam por nossa conta.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. REDUÇÃO DE RISCO -->
    <section class="section-padding text-center" style="background: var(--bg-surface); padding-top: 60px; padding-bottom: 60px;">
        <div class="container reveal">
            <h2 style="font-size: 2.8rem; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; color: var(--text-main); margin-bottom: 12px; letter-spacing: -0.02em;">Sem pagar no escuro.</h2>
            <p style="font-size: 1.25rem; color: var(--text-muted); max-width: 500px; margin: 0 auto; line-height: 1.5;">
                Você primeiro vê o resultado.<br>Só depois de aprovar o design é que paga a taxa de setup.
            </p>
        </div>
    </section>
"""
with io.open('body_p2.txt', 'w', encoding='utf-8') as f:
    f.write(body)
