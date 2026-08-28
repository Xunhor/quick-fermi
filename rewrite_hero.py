import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HERO SECTION
html = re.sub(
    r'<h1 class="hero-headline">.*?</h1>',
    '<h1 class="hero-headline">Seu negócio merece<br>um site profissional.</h1>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p class="hero-subtext">.*?</p>',
    '<p class="hero-subtext" style="max-width: 640px; font-size: 1.15rem; margin-bottom: 40px;">Criamos, publicamos e cuidamos do seu site por uma assinatura mensal. Você envia as informações pelo WhatsApp e recebe tudo pronto em até 3 dias.</p>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<a href="#modelos" class="btn btn-primary btn-large">Ver Modelos Prontos <i class="fa-solid fa-arrow-right"></i></a>',
    '<a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20saber%20mais%20sobre%20os%20sites%20da%20Boomo." class="btn btn-primary btn-large btn-whatsapp">Quero meu site <i class="fa-brands fa-whatsapp"></i></a>',
    html
)

html = re.sub(
    r'<a href="https://wa.me/559192432044\?text=Ol.*?Falar Direto no WhatsApp</a>',
    '<a href="#modelos" class="btn btn-secondary btn-large">Ver exemplos <i class="fa-solid fa-arrow-down"></i></a>',
    html, flags=re.DOTALL
)

# Insert Risk Reduction under CTA
risk_reduction = '''
<div class="hero-trust-inline reveal delay-1" style="border: none; background: transparent; padding: 0; margin-top: 24px; display: inline-flex;">
    <span class="trust-inline-item" style="font-size: 0.95rem; font-weight: 500; color: var(--text-main);">
        <i class="fa-solid fa-check" style="color: #10B981;"></i> Você aprova o design antes de pagar o setup.
    </span>
</div>
'''
html = re.sub(r'(<div class="hero-actions".*?</div>)', r'\1\n' + risk_reduction, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
