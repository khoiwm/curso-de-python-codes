msg = input('digite algo: ')
print(f'o seu tipo primitivo é {type(msg)}')
print(f'é numérico? {msg.isnumeric()}')
print(f'tem letras? {msg.isalpha()}')
print(f'tem minúsculas? {msg.islower()}')
print(f'tem maiúsculas? {msg.isupper()}')
print(f'tem letras e numéros? {msg.isalnum()}')
print(f'é um decimal? {msg.isdecimal()}')
print(f'somente espaços? {msg.isspace()}')
print(f'está capitalizada? {msg.istitle()}')
