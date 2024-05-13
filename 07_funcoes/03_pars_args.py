''''
def boas_vindas_marcos():
    print('Olá Marcos!')
    print('Temos 5 laptops em estoque.')

def boas_vindas_ronaldo():
    print('Olá Ronaldo!')
    print('Temos 4 laptops em estoque.')

def boas_vindas_linda():
    print('Olá Linda!')
    print('Temos 1 laptops em estoque.')

boas_vindas_marcos()
boas_vindas_ronaldo()
boas_vindas_linda()
'''


def boas_vindas(nome, quantidade):
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} laptops em estoque.')


boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 3)
boas_vindas('Linda', 1)
