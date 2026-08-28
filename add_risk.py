import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

risk_reduction = """
    <!-- 6. REDUÇÃO DE RISCO -->
    <section class="section-padding text-center" style="background: var(--bg-surface); border-top: 1px solid var(--border-color); padding-top: 60px; padding-bottom: 60px;">
        <div class="container reveal">
            <h2 style="font-size: 2.8rem; font-weight: 800; color: var(--text-main); margin-bottom: 12px; letter-spacing: -0.02em;">Sem pagar no escuro.</h2>
            <p style="font-size: 1.25rem; color: var(--text-muted); max-width: 500px; margin: 0 auto; line-height: 1.5;">
                Você primeiro vê o resultado.<br>Só depois de aprovar o design é que paga a taxa de setup.
            </p>
        </div>
    </section>
"""

# Replace ALL-INCLUSIVE and GUARANTEES temporarily (we will add Technology back later)
html = re.sub(
    r'<!-- 5\.1\. TUDO INCLUSO \(All-Inclusive Feature Grid\) -->.*?(?=<!-- 6\. PRICING -->)',
    risk_reduction + '\n      ',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
