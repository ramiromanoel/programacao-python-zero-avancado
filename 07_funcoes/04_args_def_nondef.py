
def boas_vindas(nome, quantidade=5): # non-default sempre vem antes do default.
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} laptops em estoque.')


boas_vindas('Marcos')
