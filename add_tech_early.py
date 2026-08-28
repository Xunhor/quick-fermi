import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tech_and_early = """
    <!-- 8. TECNOLOGIA -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--border-color);">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Tecnologia que trabalha nos bastidores.</h2>
                <p>Nós usamos a mesma infraestrutura das gigantes da tecnologia para que você não precise se preocupar com problemas técnicos.</p>
            </div>
            
            <div class="all-inclusive-grid reveal delay-1" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-rocket"></i></div>
                    <div class="inclusive-text">
                        <h4>Sites rápidos e otimizados</h4>
                        <p>Performance focada para proporcionar uma experiência rápida no celular e no desktop.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-magnifying-glass"></i></div>
                    <div class="inclusive-text">
                        <h4>Preparado para buscas</h4>
                        <p>Estrutura otimizada para ajudar clientes a encontrarem sua empresa no Google.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-shield-check"></i></div>
                    <div class="inclusive-text">
                        <h4>Segurança e estabilidade</h4>
                        <p>Seu site disponível quando seus clientes precisarem, protegido globalmente.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-mobile-screen"></i></div>
                    <div class="inclusive-text">
                        <h4>Perfeito no celular</h4>
                        <p>Experiência responsiva garantida em qualquer smartphone ou computador.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. EARLY ADOPTERS -->
    <section class="section-padding text-center" style="padding-top: 80px; padding-bottom: 80px;">
        <div class="container reveal">
            <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 16px; color: var(--accent-cyan);">Seja um dos primeiros.</h2>
            <p style="font-size: 1.1rem; color: var(--text-muted); max-width: 600px; margin: 0 auto 32px; line-height: 1.6;">
                Estamos selecionando os primeiros negócios para fazer parte da Boomo.<br>
                Temos <strong>condições especiais</strong> durante a nossa fase inicial.
            </p>
            <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20aproveitar%20as%20condi%C3%A7%C3%B5es%20especiais%20para%20os%20primeiros%20clientes." target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="padding: 12px 32px; font-size: 1.05rem;">Quero aproveitar a oportunidade <i class="fa-solid fa-arrow-right"></i></a>
        </div>
    </section>
"""

html = html.replace('<!-- 7. FAQ -->', tech_and_early + '\n    <!-- 7. FAQ -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
