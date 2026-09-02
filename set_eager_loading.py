with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

count = c.count('loading="lazy"')
print('Lazy count:', count)
c = c.replace('loading="lazy"', 'loading="eager"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Replaced all loading=lazy with eager!')
