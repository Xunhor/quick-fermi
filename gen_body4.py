import io

body = """
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

    <!-- 10. FAQ -->
    <section id="faq" class="section-padding faq-section" style="background: var(--bg-secondary); border-top: 1px solid var(--border-color);">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Perguntas Frequentes</h2>
                <p>Tire suas dúvidas antes de dar o próximo passo.</p>
            </div>
            <div class="faq-container">
                <div class="faq-item reveal delay-1">
                    <button class="faq-question">O que está incluso na assinatura? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>Absolutamente tudo que seu site precisa para funcionar: criação do design, hospedagem rápida, certificado de segurança (SSL) e suporte para manutenções e atualizações.</p></div>
                </div>
                <div class="faq-item reveal delay-2">
                    <button class="faq-question">Preciso comprar um domínio? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>Se você escolher o Plano Profissional ou Premium, o registro e a renovação anual do seu domínio (.com.br) já estão inclusos. Se você já tem um domínio, nós apenas o conectamos ao seu novo site.</p></div>
                </div>
                <div class="faq-item reveal delay-3">
                    <button class="faq-question">Quanto tempo demora para o site ficar pronto? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>A partir do momento em que você envia as informações básicas do seu negócio pelo WhatsApp (textos e fotos), nós entregamos a primeira versão para sua aprovação em até 3 dias úteis.</p></div>
                </div>
                <div class="faq-item reveal delay-4">
                    <button class="faq-question">Posso pedir alterações no site? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>Sim. Os planos incluem alterações ilimitadas dentro do escopo do site (como trocar um telefone, atualizar fotos ou textos e mudar preços). Você envia no WhatsApp e nós fazemos.</p></div>
                </div>
                <div class="faq-item reveal delay-5">
                    <button class="faq-question">Existe fidelidade? Posso cancelar? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>Não há tempo mínimo de permanência (fidelidade) e nenhuma multa rescisória. Você pode cancelar sua assinatura a qualquer momento com um simples aviso no WhatsApp.</p></div>
                </div>
                <div class="faq-item reveal delay-6">
                    <button class="faq-question">O que acontece se eu quiser sair da Boomo? O site fica meu? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer"><p>A Boomo fornece o site como um serviço por assinatura (incluindo código, hospedagem e atualizações). Caso você cancele, o serviço é desligado e o site sai do ar. O domínio (ex: suaempresa.com.br), no entanto, é sempre seu.</p></div>
                </div>
            </div>
        </div>
    </section>

    <!-- 11. CTA FINAL -->
    <section class="section-padding text-center" style="padding-top: 100px; padding-bottom: 120px;">
        <div class="container reveal">
            <h2 style="font-size: 3rem; font-weight: 800; font-family: 'Plus Jakarta Sans', sans-serif; letter-spacing: -0.04em; margin-bottom: 16px;">Pronto para colocar seu negócio no ar?</h2>
            <p style="font-size: 1.25rem; color: var(--text-muted); max-width: 600px; margin: 0 auto 40px;">
                Seu próximo cliente pode estar procurando por você agora. Tenha um site profissional sem pagar milhares de reais para uma agência.
            </p>
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20saber%20mais%20sobre%20os%20sites%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-large btn-whatsapp">Quero meu site <i class="fa-brands fa-whatsapp"></i></a>
                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20tirar%20uma%20d%C3%BAvida." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-large">Falar pelo WhatsApp</a>
            </div>
        </div>
    </section>

    <!-- 12. FOOTER -->
    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; <span id="current-year"></span> Boomo. Todos os direitos reservados.</p>
                <div class="footer-socials">
                    <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        document.getElementById('current-year').textContent = new Date().getFullYear();
        const revealElements = document.querySelectorAll('.reveal');
        if ('IntersectionObserver' in window) {
            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, { root: null, threshold: 0.1, rootMargin: "0px 0px -50px 0px" });
            revealElements.forEach(el => revealObserver.observe(el));
        } else {
            revealElements.forEach(el => el.classList.add('revealed'));
        }
        
        document.addEventListener('mousemove', (e) => {
            document.documentElement.style.setProperty('--global-mouse-x', e.clientX + 'px');
            document.documentElement.style.setProperty('--global-mouse-y', e.clientY + 'px');
        });

        document.querySelectorAll('.faq-question').forEach(button => {
            button.addEventListener('click', () => {
                const faqItem = button.parentElement;
                const isActive = faqItem.classList.contains('active');
                document.querySelectorAll('.faq-item').forEach(item => {
                    item.classList.remove('active');
                    item.querySelector('.faq-question i').className = 'fa-solid fa-plus';
                });
                if (!isActive) {
                    faqItem.classList.add('active');
                    faqItem.querySelector('.faq-question i').className = 'fa-solid fa-minus';
                }
            });
        });

        // Carousel Spotlight Logic
        document.querySelectorAll('.has-spotlight').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                card.style.setProperty('--mouse-x', ${e.clientX - rect.left}px);
                card.style.setProperty('--mouse-y', ${e.clientY - rect.top}px);
            });
        });

        const track = document.getElementById('carousel-track');
        const slides = document.querySelectorAll('.carousel-slide');
        const pills = document.querySelectorAll('.carousel-pill');
        const prevBtn = document.getElementById('carousel-prev');
        const nextBtn = document.getElementById('carousel-next');

        if (track && slides.length > 0) {
            let currentIndex = 0;
            const totalSlides = slides.length;
            function updateCarousel(index) {
                pills.forEach(p => p.classList.remove('active'));
                slides.forEach(s => s.classList.remove('active'));
                pills[index].classList.add('active');
                slides[index].classList.add('active');
                track.style.transform = 	ranslateX(-px);
                prevBtn.disabled = index === 0;
                nextBtn.disabled = index === totalSlides - 1;
            }
            pills.forEach((pill, idx) => pill.addEventListener('click', () => updateCarousel(currentIndex = idx)));
            prevBtn.addEventListener('click', () => currentIndex > 0 && updateCarousel(--currentIndex));
            nextBtn.addEventListener('click', () => currentIndex < totalSlides - 1 && updateCarousel(++currentIndex));
            window.addEventListener('resize', () => updateCarousel(currentIndex));
            updateCarousel(0);
        }
    </script>
    <script src="assets/js/menu.js"></script>
</body>
"""
with io.open('body_p4.txt', 'w', encoding='utf-8') as f:
    f.write(body)
