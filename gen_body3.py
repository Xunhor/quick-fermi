import io

body = """
    <!-- 7. PLANOS -->
    <section id="planos" class="section-padding pricing-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Assinatura simples e transparente.</h2>
                <p>Escolha o plano ideal para o momento da sua empresa.</p>
            </div>
            <div class="pricing-grid">
                <!-- Essencial -->
                <div class="price-card has-spotlight reveal delay-1">
                    <h3>Essencial</h3>
                    <p class="price-desc" style="font-size: 0.95rem;">Para quem precisa colocar seu negócio no ar rapidamente.</p>
                    <div class="price-val">R$ 149 <span>/mês</span></div>
                    <div class="price-setup">+ taxa única de setup de R$ 300</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-check"></i> 1 Página de alta conversão</li>
                        <li><i class="fa-solid fa-check"></i> Botão do WhatsApp flutuante</li>
                        <li><i class="fa-solid fa-check"></i> Hospedagem inclusa</li>
                        <li><i class="fa-solid fa-check"></i> Suporte técnico via chat</li>
                    </ul>
                    <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Essencial%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Começar Essencial</a>
                </div>
                <!-- Pro -->
                <div class="price-card featured has-spotlight reveal delay-2">
                    <span class="featured-badge"><i class="fa-solid fa-bolt"></i> Recomendado</span>
                    <h3>Profissional</h3>
                    <p class="price-desc" style="font-size: 0.95rem;">Para empresas que querem uma presença digital mais completa.</p>
                    <div class="price-val">R$ 249 <span>/mês</span></div>
                    <div class="price-setup">+ taxa única de setup de R$ 500</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-check"></i> Até 5 Páginas internas</li>
                        <li><i class="fa-solid fa-check"></i> Domínio .com.br incluso</li>
                        <li><i class="fa-solid fa-check"></i> Configuração de SEO local</li>
                        <li><i class="fa-solid fa-check"></i> Alterações ilimitadas no escopo</li>
                    </ul>
                    <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Profissional%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-full">Começar Profissional</a>
                </div>
                <!-- Premium -->
                <div class="price-card has-spotlight reveal delay-3">
                    <h3>Premium</h3>
                    <p class="price-desc" style="font-size: 0.95rem;">Para negócios que precisam de mais personalização e recursos.</p>
                    <div class="price-val">R$ 399 <span>/mês</span></div>
                    <div class="price-setup">Setup sob consulta</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-check"></i> Site corporativo robusto</li>
                        <li><i class="fa-solid fa-check"></i> Sistema de agendamento online</li>
                        <li><i class="fa-solid fa-check"></i> Integração com sistemas (API)</li>
                        <li><i class="fa-solid fa-check"></i> Gerente de conta exclusivo</li>
                    </ul>
                    <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Premium%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Falar com Consultor</a>
                </div>
            </div>
        </div>
    </section>

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
                        <h4>Sites rápidos e otimizados</h4><p>Performance focada para proporcionar uma experiência rápida no celular e no desktop.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-magnifying-glass"></i></div>
                    <div class="inclusive-text">
                        <h4>Preparado para buscas</h4><p>Estrutura otimizada para ajudar clientes a encontrarem sua empresa no Google.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-shield-check"></i></div>
                    <div class="inclusive-text">
                        <h4>Segurança e estabilidade</h4><p>Seu site disponível quando seus clientes precisarem, protegido globalmente.</p>
                    </div>
                </div>
                <div class="inclusive-item has-spotlight">
                    <div class="inclusive-icon"><i class="fa-solid fa-mobile-screen"></i></div>
                    <div class="inclusive-text">
                        <h4>Perfeito no celular</h4><p>Experiência responsiva garantida em qualquer smartphone ou computador.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
with io.open('body_p3.txt', 'w', encoding='utf-8') as f:
    f.write(body)
