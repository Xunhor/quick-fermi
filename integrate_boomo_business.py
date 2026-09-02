from bs4 import BeautifulSoup
import re

print("Starting integrate_boomo_business.py...")

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# =========================================================================
# 1. HERO HEADLINE & SUBTEXT
# =========================================================================
hero = soup.find('section', id='homepage-hero')
if hero:
    h1 = hero.find('h1')
    if h1:
        h1.string = "Um site profissional para o seu negócio acontecer"
    
    # CTA button
    btn = hero.find('a', class_='homepage-hero__cta')
    if btn:
        btn['href'] = '#planos'
        btn_text = btn.find('span')
        if btn_text:
            btn_text.string = "QUERO MEU SITE"
        else:
            btn.string = "QUERO MEU SITE"
            
    # Subtext
    sub = hero.find('p', class_='homepage-hero__subtext')
    if sub:
        sub.string = "A Boomo cria, publica e mantém o site da sua empresa por assinatura. Cuidamos de tudo para você focar no seu negócio."

    # Hero stats (Replace fake Squarespace claims with Boomo value props)
    stats = hero.find(class_='homepage-hero__stats')
    if stats:
        cards = stats.find_all(class_='stats__card')
        if len(cards) >= 3:
            # Card 1: 100% Aprovação antes do setup
            c1_stat = cards[0].find(class_='stats__card-localized-counter')
            c1_label = cards[0].find_all('p')[-1]
            if c1_stat: c1_stat.string = "100%"
            if c1_label: c1_label.string = "aprovação antes do setup"
            for st in cards[0].find_all(class_='stats__counter--static'):
                st.string = "100%"

            # Card 2: Zero Preocupação técnica
            c2_stat = cards[1].find(class_='stats__card-localized-counter')
            c2_label = cards[1].find_all('p')[-1]
            if c2_stat: c2_stat.string = "Zero"
            if c2_label: c2_label.string = "preocupação técnica"
            for st in cards[1].find_all(class_='stats__counter--static'):
                st.string = "Zero"

            # Card 3: 24/7 Hospedagem e SSL inclusos
            c3_stat = cards[2].find(class_='stats__card-localized-counter')
            c3_label = cards[2].find_all('p')[-1]
            if c3_stat: c3_stat.string = "24/7"
            if c3_label: c3_label.string = "hospedagem e SSL inclusos"
            for st in cards[2].find_all(class_='stats__counter--static'):
                st.string = "24/7"
            cards[2]['class'] = [cls for cls in cards[2].get('class', []) if cls != 'stats__card--mobile-hide']

        # Label above stats
        stats_intro = hero.find('p', class_='homepage-hero__stats-intro')
        if stats_intro:
            stats_intro.string = "O modelo por assinatura que simplifica a presença digital da sua marca."

# =========================================================================
# 2. GET-STARTED SECTION (Replace AI builder with Boomo's Hands-off Service)
# =========================================================================
gs = soup.find('section', id='get-started')
if gs:
    title = gs.find('h2', class_='headline__title')
    if title:
        title.string = "Um processo simples e direto. Sem perda de tempo."
    body = gs.find('p', class_='headline__body')
    if body:
        body.string = "Você cuida dos seus clientes, a equipe Boomo cuida de todo o design e publicação do seu site."

    cards = gs.find_all(class_='ai-entrypoints__card')
    if len(cards) >= 2:
        # Card 1
        c1_title = cards[0].find('h3')
        if c1_title: c1_title.string = "Criação sob medida pela nossa equipe"
        c1_body = cards[0].find('p', class_='text--footnote')
        if c1_body: c1_body.string = "Esqueça templates complicados ou horas tentando mexer em blocos. Nós formatamos e publicamos todo o conteúdo para você."
        c1_cta = cards[0].find('a', class_='ai-entrypoints__cta')
        if c1_cta:
            c1_cta['href'] = "https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20saber%20mais%20sobre%20a%20cria%C3%A7%C3%A3o%20de%20sites%20da%20Boomo."
            c1_cta_text = c1_cta.find('span')
            if c1_cta_text: c1_cta_text.string = "Falar no WhatsApp"

        # Card 2
        c2_title = cards[1].find('h3')
        if c2_title: c2_title.string = "Modelos pensados para conversão"
        c2_body = cards[1].find('p', class_='text--footnote')
        if c2_body: c2_body.string = "Projetados para clínicas, escritórios, consultorias e empresas locais com design de alto padrão."
        c2_cta = cards[1].find('a', class_='ai-entrypoints__cta')
        if c2_cta:
            c2_cta['href'] = "#planos"
            c2_cta_text = c2_cta.find('span')
            if c2_cta_text: c2_cta_text.string = "Conhecer os planos"

# =========================================================================
# 3. CUSTOMERS-SERVED SECTION (Replace 14M claim)
# =========================================================================
cs = soup.find('section', id='customers-served')
if cs:
    cs_title = cs.find('h2')
    if cs_title:
        cs_title.string = "O padrão de sofisticação que o seu negócio precisa no digital"

# =========================================================================
# 4. MADE-WITH-SQSP / VITRINE
# =========================================================================
mws = soup.find('section', id='made-with-sqsp')
if mws:
    mws_title = mws.find(['h2', 'h3'])
    if mws_title:
        mws_title.string = "Exemplos de sites que podemos criar"

# =========================================================================
# 5. INJECT PRICING SECTION (#planos)
# =========================================================================
# Remove existing #planos if present
existing_planos = soup.find('section', id='planos')
if existing_planos:
    existing_planos.decompose()

pricing_html = '''
<section id="planos" class="boomo-pricing-section" style="background-color: #000000; padding: 120px 24px; color: #FFFFFF; font-family: Clarkson, -apple-system, sans-serif; position: relative;">
    <div style="max-width: 1200px; margin: 0 auto;">
        
        <!-- Header -->
        <div style="text-align: center; max-width: 680px; margin: 0 auto 64px auto;">
            <p style="font-size: 13px; text-transform: uppercase; letter-spacing: 0.15em; color: #10B981; font-weight: 700; margin-bottom: 12px;">Planos & Assinaturas</p>
            <h2 style="font-size: clamp(32px, 4vw, 44px); font-weight: 700; letter-spacing: -0.03em; line-height: 1.15; margin-bottom: 20px; color: #FFFFFF;">
                Planos transparentes. Sem surpresas.
            </h2>
            <p style="font-size: 16px; line-height: 1.6; color: rgba(255, 255, 255, 0.65); margin: 0;">
                Uma assinatura mensal completa que inclui criação profissional, hospedagem de alta velocidade, manutenção e suporte contínuo.
            </p>
        </div>

        <!-- Cards Grid -->
        <div class="boomo-pricing-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; align-items: stretch; margin-bottom: 48px;">
            
            <!-- Plano Essencial -->
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 8px; padding: 40px 32px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">
                <div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Essencial</h3>
                    <p style="font-size: 14px; color: rgba(255, 255, 255, 0.6); min-height: 42px; margin-bottom: 24px;">
                        Ideal para autônomos e pequenos negócios que buscam uma presença profissional sólida.
                    </p>
                    
                    <div style="display: flex; align-items: baseline; gap: 4px; margin-bottom: 6px;">
                        <span style="font-size: 20px; font-weight: 600; color: rgba(255, 255, 255, 0.75);">R$</span>
                        <span style="font-size: 44px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.03em;">149</span>
                        <span style="font-size: 15px; color: rgba(255, 255, 255, 0.5);">/mês</span>
                    </div>
                    <p style="font-size: 13px; color: rgba(255, 255, 255, 0.5); padding-bottom: 24px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 28px;">
                        Setup único de R$ 300 (após aprovação)
                    </p>

                    <ul style="list-style: none; padding: 0; margin: 0 0 32px 0; display: flex; flex-direction: column; gap: 14px; font-size: 14px; color: rgba(255, 255, 255, 0.85);">
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Site One-Page profissional
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> 100% responsivo (desktop e mobile)
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Hospedagem rápida e SSL inclusos
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Integração direta com WhatsApp
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Manutenção e suporte mensal
                        </li>
                    </ul>
                </div>

                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20contratar%20o%20Plano%20Essencial%20da%20Boomo." target="_blank" style="display: block; text-align: center; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; text-decoration: none; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px; transition: background 0.2s;">
                    Quero o Essencial
                </a>
            </div>

            <!-- Plano Pro Negócios Locais (Featured) -->
            <div style="background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(16, 185, 129, 0.6); border-radius: 8px; padding: 40px 32px; display: flex; flex-direction: column; justify-content: space-between; position: relative; box-shadow: 0 16px 48px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(16, 185, 129, 0.2);">
                <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #10B981; color: #000000; font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; padding: 4px 16px; border-radius: 999px;">
                    Mais Escolhido
                </div>

                <div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Pro Negócios Locais</h3>
                    <p style="font-size: 14px; color: rgba(255, 255, 255, 0.6); min-height: 42px; margin-bottom: 24px;">
                        Para empresas, clínicas e escritórios que precisam de autoridade e páginas dedicadas.
                    </p>
                    
                    <div style="display: flex; align-items: baseline; gap: 4px; margin-bottom: 6px;">
                        <span style="font-size: 20px; font-weight: 600; color: rgba(255, 255, 255, 0.75);">R$</span>
                        <span style="font-size: 44px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.03em;">249</span>
                        <span style="font-size: 15px; color: rgba(255, 255, 255, 0.5);">/mês</span>
                    </div>
                    <p style="font-size: 13px; color: rgba(255, 255, 255, 0.5); padding-bottom: 24px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 28px;">
                        Setup único de R$ 500 (após aprovação)
                    </p>

                    <ul style="list-style: none; padding: 0; margin: 0 0 32px 0; display: flex; flex-direction: column; gap: 14px; font-size: 14px; color: rgba(255, 255, 255, 0.9);">
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> <strong>Tudo do plano Essencial</strong>
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Estrutura Multi-páginas (até 5 páginas)
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Otimização para SEO e Google Meu Negócio
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Formulário de contato e agendamento
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Alterações mensais de conteúdo inclusas
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Suporte prioritário via WhatsApp
                        </li>
                    </ul>
                </div>

                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20contratar%20o%20Plano%20Pro%20Neg%C3%B3cios%20Locais%20da%20Boomo." target="_blank" style="display: block; text-align: center; background: #FFFFFF; color: #000000; text-decoration: none; padding: 14px; border-radius: 4px; font-weight: 700; font-size: 14px; transition: transform 0.2s, background 0.2s;">
                    Quero o Pro Negócios Locais
                </a>
            </div>

            <!-- Plano Personalizado -->
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 8px; padding: 40px 32px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">
                <div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Personalizado</h3>
                    <p style="font-size: 14px; color: rgba(255, 255, 255, 0.6); min-height: 42px; margin-bottom: 24px;">
                        Para projetos que exigem funcionalidades específicas, catálogos ou integrações exclusivas.
                    </p>
                    
                    <div style="display: flex; align-items: baseline; gap: 4px; margin-bottom: 6px;">
                        <span style="font-size: 20px; font-weight: 600; color: rgba(255, 255, 255, 0.75);">R$</span>
                        <span style="font-size: 44px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.03em;">399</span>
                        <span style="font-size: 15px; color: rgba(255, 255, 255, 0.5);">/mês</span>
                    </div>
                    <p style="font-size: 13px; color: rgba(255, 255, 255, 0.5); padding-bottom: 24px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 28px;">
                        Setup sob consulta (após aprovação)
                    </p>

                    <ul style="list-style: none; padding: 0; margin: 0 0 32px 0; display: flex; flex-direction: column; gap: 14px; font-size: 14px; color: rgba(255, 255, 255, 0.85);">
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> <strong>Design 100% exclusivo e sob medida</strong>
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Catálogo de produtos ou portfólio rico
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Integrações com CRMs e ferramentas externas
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Consultoria de conversão dedicada
                        </li>
                        <li style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #10B981; font-weight: bold;">✓</span> Suporte e alterações sob demanda
                        </li>
                    </ul>
                </div>

                <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20um%20projeto%20Personalizado%20com%20a%20Boomo." target="_blank" style="display: block; text-align: center; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; text-decoration: none; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px; transition: background 0.2s;">
                    Falar com consultor
                </a>
            </div>

        </div>

        <!-- Trust Guarantee Banner (Regra 13) -->
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 28px 36px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div style="max-width: 760px;">
                <h4 style="font-size: 17px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
                    <span style="color: #10B981; font-size: 20px;">🛡️</span> Garantia de Aprovação Risco Zero
                </h4>
                <p style="font-size: 14px; color: rgba(255, 255, 255, 0.7); margin: 0; line-height: 1.5;">
                    Nós desenhamos o site da sua empresa primeiro. Você avalia e aprova cada detalhe visual antes de pagar a taxa de setup. Se não aprovar, não paga nada.
                </p>
            </div>
            <a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20iniciar%20meu%20site%20com%20a%20Garantia%20de%20Aprova%C3%A7%C3%A3o%20da%20Boomo." target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #10B981; color: #000000; font-weight: 700; font-size: 13px; text-decoration: none; padding: 12px 24px; border-radius: 4px; white-space: nowrap;">
                Iniciar sem compromisso →
            </a>
        </div>

    </div>
</section>
'''

faq_section = soup.find('section', id='homepage-faq')
if faq_section:
    new_pricing_soup = BeautifulSoup(pricing_html, 'html.parser')
    faq_section.insert_before(new_pricing_soup)
    print("Inserted #planos right before #homepage-faq!")

# =========================================================================
# 6. UPDATE FAQ QUESTIONS & ANSWERS (Regras 1, 7 & 12)
# =========================================================================
boomo_faqs = [
    {
        "q": "Como funciona a assinatura da Boomo?",
        "a": "A Boomo cria, publica e cuida de toda a parte técnica do site da sua empresa através de uma assinatura mensal. Você só precisa nos enviar as informações e fotos do seu negócio. Nossa equipe desenvolve o layout profissional, configura a hospedagem, o certificado SSL e coloca tudo no ar."
    },
    {
        "q": "Preciso pagar a taxa de setup antes de ver o site?",
        "a": "Não. Trabalhamos com Garantia de Aprovação: nós desenvolvemos a primeira versão do seu site e você só paga o setup após aprovar o design. Se você não gostar do resultado, não tem custo algum."
    },
    {
        "q": "O que está incluso na mensalidade?",
        "a": "Está inclusa a hospedagem de alta performance, certificado de segurança SSL, monitoramento contínuo, manutenção preventiva contra falhas e alterações mensais de textos, fotos e novidades da sua empresa diretamente pelo WhatsApp."
    },
    {
        "q": "Posso cancelar a assinatura quando quiser?",
        "a": "Sim. Nossos planos não possuem contrato de fidelidade forçada. Você pode solicitar o cancelamento a qualquer momento sem burocracia ou multas abusivas."
    },
    {
        "q": "E se eu já tiver um domínio registrado (.com.br ou .com)?",
        "a": "Nós configuramos e apontamos o seu domínio existente sem nenhum custo adicional. Se você ainda não tiver um domínio, nós orientamos e auxiliamos no registro oficial em seu nome ou no CNPJ da sua empresa."
    },
    {
        "q": "Em quanto tempo meu site fica pronto?",
        "a": "Após você nos enviar as informações e materiais essenciais da sua empresa, entregamos a primeira versão completa do site para a sua aprovação em poucos dias úteis."
    }
]

if faq_section:
    # Update FAQ title
    faq_h2 = faq_section.find('h2')
    if faq_h2:
        faq_h2.string = "Perguntas frequentes sobre a Boomo"

    # Find accordion bodies
    accordion_items = faq_section.find_all(class_='faq__accordion-item')
    for i, item in enumerate(accordion_items):
        if i < len(boomo_faqs):
            # Question
            q_btn = item.find('button', class_='global-navigation__accordion-heading') or item.find('button')
            if q_btn:
                q_span = q_btn.find('span')
                if q_span:
                    q_span.string = boomo_faqs[i]["q"]
                else:
                    q_btn.string = boomo_faqs[i]["q"]
            
            # Answer
            body_div = item.find(class_='faq__accordion-body-wrapper') or item.find(class_='faq__accordion-body') or item.find('p')
            if body_div:
                p_tag = body_div.find('p')
                if p_tag:
                    p_tag.string = boomo_faqs[i]["a"]
                else:
                    body_div.string = boomo_faqs[i]["a"]
        else:
            # Remove redundant FAQ items beyond the 6 core questions
            item.decompose()

# =========================================================================
# 7. CONVERSION CTA (Particle sphere section at bottom)
# =========================================================================
conv = soup.find('section', id='conversion')
if conv:
    c_title = conv.find(['h2', 'h1'])
    if c_title:
        c_title.string = "Coloque o seu site profissional no ar"
    c_sub = conv.find('p')
    if c_sub:
        c_sub.string = "Fale conosco no WhatsApp, aprove o design primeiro e tenha seu site completo por assinatura mensal."
    c_btn = conv.find('a', class_='conversion__cta')
    if c_btn:
        c_btn['href'] = "https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20colocar%20o%20meu%20site%20profissional%20no%20ar%20com%20a%20Boomo."
        c_btn_text = c_btn.find('span')
        if c_btn_text:
            c_btn_text.string = "Falar no WhatsApp"

# =========================================================================
# 8. TOP NAVIGATION LINKS
# =========================================================================
nav = soup.find('nav', class_='global-navigation__nav')
if nav:
    buttons = nav.find_all('button', class_='global-navigation__header-link-item')
    if len(buttons) >= 3:
        b0_span = buttons[0].find('span')
        if b0_span: b0_span.string = "Recursos"
        buttons[0]['onclick'] = "document.getElementById('one-platform').scrollIntoView({behavior:'smooth'})"

        b1_span = buttons[1].find('span')
        if b1_span: b1_span.string = "Como Funciona"
        buttons[1]['onclick'] = "document.getElementById('get-started').scrollIntoView({behavior:'smooth'})"

        b2_span = buttons[2].find('span')
        if b2_span: b2_span.string = "Planos"
        buttons[2]['onclick'] = "document.getElementById('planos').scrollIntoView({behavior:'smooth'})"

    # Remove preise link
    preise = nav.find('a', class_='global-navigation__pricing-german')
    if preise:
        preise.decompose()

# Save final index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("integrate_boomo_business.py executed successfully!")
