import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_content = """
            <div class="faq-container">
                <div class="faq-item reveal delay-1">
                    <button class="faq-question">O que está incluso na assinatura? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>Absolutamente tudo que seu site precisa para funcionar: criação do design, hospedagem rápida, certificado de segurança (SSL) e suporte para manutenções e atualizações.</p>
                    </div>
                </div>
                
                <div class="faq-item reveal delay-2">
                    <button class="faq-question">Preciso comprar um domínio? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>Se você escolher o Plano Profissional ou Premium, o registro e a renovação anual do seu domínio (.com.br) já estão inclusos. Se você já tem um domínio, nós apenas o conectamos ao seu novo site.</p>
                    </div>
                </div>

                <div class="faq-item reveal delay-3">
                    <button class="faq-question">Quanto tempo demora para o site ficar pronto? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>A partir do momento em que você envia as informações básicas do seu negócio pelo WhatsApp (textos e fotos), nós entregamos a primeira versão para sua aprovação em até 3 dias.</p>
                    </div>
                </div>

                <div class="faq-item reveal delay-4">
                    <button class="faq-question">Posso pedir alterações no site? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>Sim. Os planos incluem alterações ilimitadas dentro do escopo do site (como trocar um telefone, atualizar fotos ou textos e mudar preços). Você envia no WhatsApp e nós fazemos.</p>
                    </div>
                </div>

                <div class="faq-item reveal delay-5">
                    <button class="faq-question">Existe fidelidade? Posso cancelar? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>Não há tempo mínimo de permanência (fidelidade) e nenhuma multa rescisória. Você pode cancelar sua assinatura a qualquer momento com um simples aviso no WhatsApp.</p>
                    </div>
                </div>
                
                <div class="faq-item reveal delay-6">
                    <button class="faq-question">O que acontece se eu quiser sair da Boomo? O site fica meu? <i class="fa-solid fa-plus"></i></button>
                    <div class="faq-answer">
                        <p>A Boomo fornece o site como um serviço por assinatura (incluindo código, hospedagem e atualizações contínuas). Caso você cancele, o serviço é desligado e o site sai do ar, assim como serviços da Netflix ou Shopify. O domínio (ex: suaempresa.com.br), no entanto, é sempre seu, e você pode usá-lo em outra plataforma se desejar.</p>
                    </div>
                </div>
            </div>
"""

html = re.sub(
    r'<div class="faq-container">.*?</div>\s*</div>\s*</section>',
    faq_content + '</div>\n    </section>',
    html, flags=re.DOTALL
)

# And add Final CTA Section before FOOTER
final_cta = """
    <!-- 11. CTA FINAL -->
    <section class="section-padding text-center" style="padding-top: 100px; padding-bottom: 120px;">
        <div class="container reveal">
            <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -0.04em; margin-bottom: 16px;">Pronto para colocar seu negócio no ar?</h2>
            <p style="font-size: 1.25rem; color: var(--text-muted); max-width: 600px; margin: 0 auto 40px;">
                Seu próximo cliente pode estar procurando por você agora. Tenha um site profissional sem pagar milhares de reais para uma agência.
            </p>
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20saber%20mais%20sobre%20os%20sites%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-large btn-whatsapp">Quero meu site <i class="fa-brands fa-whatsapp"></i></a>
                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20tirar%20uma%20d%C3%BAvida." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-large">Falar pelo WhatsApp</a>
            </div>
        </div>
    </section>
"""

html = html.replace('<!-- 8. FOOTER -->', final_cta + '\n    <!-- 8. FOOTER -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
