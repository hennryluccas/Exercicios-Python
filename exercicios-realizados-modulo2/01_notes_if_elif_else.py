#Aula if, elif e else

nome = str(input('Qual é seu nome? '))
if nome == 'Hennry':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in ['Maria', 'Joana', 'Fernanda', 'Ana', 'Paula']:
    print('Belo nome feminino.')
else:
    print('Seu nome é bem nosrmal.')
print('Tenha um bom dia, {}!'.format(nome))
