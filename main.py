print('Bem vindo a loja da Galdina Silva de Souza, RU 4370444') #identificador pessoal

valor_produto = float(input('Digite o valor unitário do produto:'))
#criei a primeira variável pro cliente inserir o valor do produto utilizando o 'float' caso tenha ponto flutuante
quantidade = int(input('Digite a quantidade desejada:'))
#criei a segunda variável pro cliente inserir a quantidade, utilizando o 'int' pois precisará retornar um valor numérico inteiro
desconto_produto = 0
#criei variável do desconto
if quantidade < 10: #utilizei o if para determinar se a quantidade for menor ou igual a 10 ter desconto de 0
    desconto_produto = 0.00
elif (quantidade >= 10) and (quantidade <= 99 ):
    #elif utilizado para criar mais uma condição, se a quantidade for maior ou igual a 10 e menor ou igual a 99 terá desconto de 5%
    desconto_produto = 0.05
elif (quantidade >= 100) and (quantidade <= 999 ):
    #último elif para se a quantidade for maior ou igual a 100 e menor ou igual a 999 ter desconto de 10%
    desconto_produto = 0.10
else:
    #else pra finalizar o desconto para uma quantidade maior que 1000 peças ser de 15%
    desconto_produto = 0.15

total_sem_desconto = valor_produto * quantidade
#variável pra calcular o valor total do pedido
print('O valor total SEM desconto é de : R${:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
#variável que vai fazer o cálculo do desconto
print('O valor do produto com desconto é de: R${:.2f}'.format(total_com_desconto))

