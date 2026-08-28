import io
import re

body = """<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="#" class="logo">Boomo.</a>
            
            <div class="nav-menu-wrapper" id="nav-menu">
                <ul class="nav-links">
                    <li><a href="#modelos" data-menu-id="modelos">Exemplos</a></li>
                    <li><a href="#como-funciona" data-menu-id="como-funciona">Como Funciona</a></li>
                    <li><a href="#planos" data-menu-id="planos">Planos</a></li>
                    <li><a href="#faq" data-menu-id="faq">FAQ</a></li>
                </ul>
                <div class="nav-mobile-cta">
                    <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20saber%20mais%20sobre%20os%20sites%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-full">Falar no WhatsApp <i class="fa-brands fa-whatsapp"></i></a>
                </div>
            </div>
            
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-pill" aria-label="Alternar Tema">
                    <span class="pill-track">
                        <span class="pill-thumb">
                            <span class="pill-icon pill-moon">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 1 1 11.21 3a7 7 0 0 0 9.79 9.79z" fill="currentColor"/></svg>
                            </span>
                            <span class="pill-icon pill-sun">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><line x1="12" y1="2" x2="12" y2="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="12" y1="20" x2="12" y2="22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="2" y1="12" x2="4" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="20" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                            </span>
                        </span>
                    </span>
                </button>
                <button id="mobile-menu-btn" class="mobile-menu-toggle" aria-label="Abrir Menu">
                    <span class="bar"></span><span class="bar"></span><span class="bar"></span>
                </button>
            </div>
        </div>
    </nav>

    <!-- 2. HERO -->
    <section class="hero">
        <div class="hero-aurora-glow"></div>
        <div class="container hero-container">
            <div class="hero-header-block text-center reveal">
                <h1 class="hero-headline">Seu negócio merece<br>um site profissional.</h1>
                <p class="hero-subtext" style="max-width: 640px; font-size: 1.15rem; margin: 0 auto 40px auto; color: var(--text-muted); line-height: 1.6;">Criamos, publicamos e cuidamos do seu site por uma assinatura mensal. Você envia as informações pelo WhatsApp e recebe tudo pronto em até 3 dias.</p>
                <div class="hero-actions" style="margin-bottom: 24px;">
                    <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20saber%20mais%20sobre%20os%20sites%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-large btn-whatsapp">Quero meu site <i class="fa-brands fa-whatsapp"></i></a>
                    <a href="#modelos" class="btn btn-secondary btn-large">Ver exemplos <i class="fa-solid fa-arrow-down"></i></a>
                </div>
                <div class="hero-trust-inline reveal delay-1" style="border: none; background: transparent; padding: 0;">
                    <span class="trust-inline-item" style="font-size: 0.95rem; font-weight: 500; color: var(--text-main);"><i class="fa-solid fa-check" style="color: #10B981;"></i> Você aprova o design antes de pagar o setup.</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. TEMPLATES -->
    <section id="modelos" class="showroom-carousel-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Sites demonstrativos</h2>
                <p>Veja alguns exemplos do que podemos criar para o seu negócio.</p>
            </div>
            
            <div class="carousel-categories-wrap reveal delay-1">
                <div class="carousel-pills" role="tablist">
                    <button class="carousel-pill active" data-index="0">
                        <i class="fa-solid fa-heart-pulse"></i> Estética & Saúde
                    </button>
                    <button class="carousel-pill" data-index="1">
                        <i class="fa-solid fa-tooth"></i> Odontologia
                    </button>
                    <button class="carousel-pill" data-index="2">
                        <i class="fa-solid fa-scale-balanced"></i> Advocacia
                    </button>
                    <button class="carousel-pill" data-index="3">
                        <i class="fa-solid fa-chart-line"></i> Contabilidade
                    </button>
                </div>
            </div>

            <div class="carousel-viewport-container reveal delay-2">
                <button class="carousel-nav-btn prev-btn" id="carousel-prev" aria-label="Modelo anterior">
                    <i class="fa-solid fa-chevron-left"></i>
                </button>
                <button class="carousel-nav-btn next-btn" id="carousel-next" aria-label="Próximo modelo">
                    <i class="fa-solid fa-chevron-right"></i>
                </button>

                <div class="carousel-track-wrapper" id="carousel-track-wrap">
                    <div class="carousel-track" id="carousel-track">
                        <!-- Slide 1: Saúde -->
                        <div class="carousel-slide active" data-index="0">
                            <div class="mockup-window-card">
                                <div class="mobile-template-card">
                                    <div class="mobile-card-image">
                                        <img src="templates/estetica/assets/images/hero-estetica.webp" alt="Estética" width="512" height="512">
                                        <div class="image-gradient-overlay"></div>
                                    </div>
                                    <div class="mobile-card-content">
                                        <div class="template-logo"><i class="fa-solid fa-spa"></i> Lumina Estética</div>
                                        <div class="template-name">Layout: Wellness & Saúde</div>
                                        <p class="template-desc">Um design limpo, focado em agendamentos pelo WhatsApp e exposição clara dos procedimentos e corpo clínico.</p>
                                        <a href="/templates/estetica" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Ver site completo <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                                    </div>
                                </div>
                                <div class="desktop-template-card">
                                    <div class="window-header-bar">
                                        <div class="traffic-lights"><span class="light red"></span><span class="light yellow"></span><span class="light green"></span></div>
                                        <div class="url-bar"><i class="fa-solid fa-lock"></i> clinica-exemplo.com.br</div>
                                        <a href="/templates/estetica" target="_blank" rel="noopener noreferrer" class="btn-visit-site">Abrir Site <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                                    </div>
                                    <div class="iframe-container"><iframe data-src="/templates/estetica" title="Preview" loading="lazy"></iframe></div>
                                </div>
                            </div>
                        </div>
                        <!-- Slide 2: Odontologia -->
                        <div class="carousel-slide" data-index="1">
                            <div class="mockup-window-card">
                                <div class="mobile-template-card">
                                    <div class="mobile-card-image">
                                        <img src="templates/odonto/assets/images/hero-odonto.webp" alt="Odonto" width="512" height="512" onerror="this.src='templates/estetica/assets/images/hero-odonto.webp'">
                                        <div class="image-gradient-overlay"></div>
                                    </div>
                                    <div class="mobile-card-content">
                                        <div class="template-logo"><i class="fa-solid fa-tooth"></i> Dra. Odonto</div>
                                        <div class="template-name">Layout: Sorriso Perfeito</div>
                                        <p class="template-desc">Ideal para dentistas. Apresenta tratamentos, depoimentos, fotos de antes/depois e facilita o agendamento.</p>
                                        <a href="/templates/odonto" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Ver site completo <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                                    </div>
                                </div>
                                <div class="desktop-template-card">
                                    <div class="window-header-bar">
                                        <div class="traffic-lights"><span class="light red"></span><span class="light yellow"></span><span class="light green"></span></div>
                                        <div class="url-bar"><i class="fa-solid fa-lock"></i> consultorio-exemplo.com.br</div>
                                        <a href="/templates/odonto" target="_blank" rel="noopener noreferrer" class="btn-visit-site">Abrir Site <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                                    </div>
                                    <div class="iframe-container"><iframe data-src="/templates/odonto" title="Preview" loading="lazy"></iframe></div>
                                </div>
                            </div>
                        </div>
                        <!-- Slide 3 & 4 (Empty) -->
                        <div class="carousel-slide" data-index="2">
                            <div class="mockup-window-card" style="background:var(--bg-secondary); display:flex; align-items:center; justify-content:center; min-height:400px;"><p style="color:var(--text-muted);"><i class="fa-solid fa-hourglass-half"></i> Em desenvolvimento</p></div>
                        </div>
                        <div class="carousel-slide" data-index="3">
                            <div class="mockup-window-card" style="background:var(--bg-secondary); display:flex; align-items:center; justify-content:center; min-height:400px;"><p style="color:var(--text-muted);"><i class="fa-solid fa-hourglass-half"></i> Em desenvolvimento</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
with io.open('body_p1.txt', 'w', encoding='utf-8') as f:
    f.write(body)
