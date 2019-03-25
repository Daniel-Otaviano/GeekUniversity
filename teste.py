#print('Hello World')

n = input('Digite seu nome: ').title()
i = int(input('Digite sua idade: '))

while True:
    s = input('Digite seu sexo: ').title()
    if (s == 'Masculino') or (s == 'Feminino'):

        if s == 'Masculino':
            print(f'Bem vindo, {n}! você nasceu em {2019 - i}')
            break
        elif s == 'Feminino':
            print(f'Bem vinda, {n}! você nasceu em {2019 - i}')
            break
    else:
        print('Digite o sexo corretamente!')

