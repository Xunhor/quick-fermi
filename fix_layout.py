import re
import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. FIX CAROUSEL IFRAMES (change data-src to src)
html = html.replace('<iframe data-src="/templates/estetica"', '<iframe src="/templates/estetica"')
html = html.replace('<iframe data-src="/templates/odonto"', '<iframe src="/templates/odonto"')

# 2. FIX FAQ STRUCTURE
faq_old_start = '<div class="faq-container">'
faq_old_end = '<!-- 11. CTA FINAL -->'

# Find the block to replace
match = re.search(r'<div class="faq-container">.*?</section>', html, flags=re.DOTALL)
if match:
    old_faq_block = match.group(0)
    
    new_faq_block = """<div class="faq-grid" itemscope itemtype="https://schema.org/FAQPage">
                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        O que está incluso na assinatura? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">Absolutamente tudo que seu site precisa para funcionar: criação do design, hospedagem rápida, certificado de segurança (SSL) e suporte para manutenções e atualizações.</p>
                    </div>
                </details>
                
                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        Preciso comprar um domínio? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">Se você escolher o Plano Profissional ou Premium, o registro e a renovação anual do seu domínio (.com.br) já estão inclusos. Se você já tem um domínio, nós apenas o conectamos ao seu novo site.</p>
                    </div>
                </details>

                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        Quanto tempo demora para o site ficar pronto? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">A partir do momento em que você envia as informações básicas do seu negócio pelo WhatsApp (textos e fotos), nós entregamos a primeira versão para sua aprovação em até 3 dias úteis.</p>
                    </div>
                </details>

                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        Posso pedir alterações no site? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">Sim. Os planos incluem alterações ilimitadas dentro do escopo do site (como trocar um telefone, atualizar fotos ou textos e mudar preços). Você envia no WhatsApp e nós fazemos.</p>
                    </div>
                </details>

                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        Existe fidelidade? Posso cancelar? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">Não há tempo mínimo de permanência (fidelidade) e nenhuma multa rescisória. Você pode cancelar sua assinatura a qualquer momento com um simples aviso no WhatsApp.</p>
                    </div>
                </details>
                
                <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <summary itemprop="name">
                        O que acontece se eu quiser sair da Boomo? O site fica meu? 
                        <div class="faq-icon-wrap"><i class="fa-solid fa-chevron-down"></i></div>
                    </summary>
                    <div class="faq-content" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p itemprop="text">A Boomo fornece o site como um serviço por assinatura (incluindo código, hospedagem e atualizações). Caso você cancele, o serviço é desligado e o site sai do ar. O domínio (ex: suaempresa.com.br), no entanto, é sempre seu.</p>
                    </div>
                </details>
            </div>
        </div>
    </section>"""
    
    html = html.replace(old_faq_block, new_faq_block)

# 3. Remove JS for the fake FAQ
html = re.sub(r'document\.querySelectorAll\(\'\.faq-question\'\)\.forEach.*?\}\);\s*\}\);\s*\}\);', '', html, flags=re.DOTALL)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("FAQ and Iframes fixed")
