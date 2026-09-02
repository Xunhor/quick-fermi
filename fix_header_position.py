with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

rule_to_add = '''
        #global-navigation {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            background: transparent !important;
            z-index: 1000 !important;
        }
        main#content, #homepage-hero {
            margin-top: 0 !important;
            padding-top: 0 !important;
            position: relative !important;
        }
        body {
            background-color: #000000 !important;
        }
'''

c = c.replace('body {', rule_to_add + '\n        body {', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Header position set to absolute and body background set to #000000!")
