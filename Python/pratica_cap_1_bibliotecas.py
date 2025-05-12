import numpy as np
from random import choice, choices, randrange
from math import pow, sqrt, pi

##############3.Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente. 

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

# numero = choice(lista)

# print(numero)

############4.Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
# numero = randrange(100)

# print(numero)

##########5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º. 

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))

# potencia = int(pow(n1, n2))

# print(potencia)


############6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

# numero_participantes = int(input("Digite o número de participantes: "))

# numero_sorteado = randrange(numero_participantes+1)

# print(numero_sorteado)

########7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

# nome = input("Digite seu nome: ")

# token = randrange(1000, 9999, 2)

# print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

#########8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

# frutas = ["maçã", "banana", "uva", "pêra", 
#           "manga", "coco", "melancia", "mamão",
#           "laranja", "abacaxi", "kiwi", "ameixa"]

# salada = choices(frutas, k=3)

# print('Parabéns! Você ganhou uma salada de frutas surpresa! Os ingredientes são: ', salada)


##########9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:

# numeros = [2, 8, 15, 23, 91, 112, 256]

# for numero in numeros:
#     raiz = sqrt(numero)
#     print(f'A raiz de {numero} é inteira? {raiz}:', raiz // 1 == raiz)
    
##########10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar. 

# raio = float(input("Digite o raio do jardim: "))

# area = pi * pow(raio, 2)

# valor = area * 25

# print(f'O valor a ser pago é de R$ {valor:.2f}')