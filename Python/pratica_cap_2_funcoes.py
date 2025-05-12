#########1. Escreva um código que lê a lista abaixo e faça:

# lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#     A leitura do tamanho da lista
#     A leitura do maior e menor valor
#     A soma dos valores da lista

# Ao final exiba uma mensagem dizendo:

# "A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"

# lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# tam = len(lista)
# maior = max(lista)
# menor = min(lista)
# soma = sum(lista)

# print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")

###############################################################################################################################################################

#########2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# Tabuada do 7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70

# def tabuada(numero):
#     for i in range(1,11):
#         print(f'{numero} x {i} = {i*numero}')

# tabuada(7)



###############################################################################################################################################################

#########3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Utilize o return na função e salve a nova lista na variável mult_3.

# lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
# mult_3 = []

# def multiplos3(lista):
#     for i in lista:
#         if i % 3 == 0:
#             mult_3.append(i)
#     return mult_3


# lista_multiplos = multiplos3(lista)

# print(lista_multiplos)

###############################################################################################################################################################

#########4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# quadrados = list(map(lambda x: pow(x,2),lista))

# print(quadrados)


###############################################################################################################################################################

#########5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"

# notas = []

# for i in range(0,5):
#     notas.append(float(input(f'Digite a {i+1}ª nota: ')))

# def calculaPontuacao(notas:list = [0]) -> float:
#     ''' Função que calcula a pontuação dos skatistas
#         notas: list, default [0]
#             lista com as notas dadas pelo juiz ao skatista
#         return = media: float
#             media calculada das notas
    
#     '''
#     notas.remove(max(notas))
#     notas.remove(min(notas))
#     media = sum(notas)/len(notas)
#     return media

# media = calculaPontuacao(notas)

# print(f"Nota da manobra: {media:.1f}")



###############################################################################################################################################################

#########6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

#     maior nota
#     menor nota
#     média
#     situação (Aprovado(a) ou Reprovado(a))

# Para testar o comportamento da função, os dados podem ser exibidos em um texto:

# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
# notas=[]
# for i in range(0,4):
#     notas.append(float(input(f'Digite a {i+1}ª nota: ')))

# def analiseDesempenho(notas):
#     maior = max(notas)
#     menor = min(notas)
#     media = sum(notas) / len(notas)


#     if media >= 6.0:
#         situacao = 'Aprovado(a)'
#     else:
#         situacao = 'Reprovado(a)'
    
#     return (maior, menor, media, situacao)

# maior, menor, media, situacao = analiseDesempenho(notas)

# print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")



###############################################################################################################################################################

#########7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# nomes_processados = map(lambda nome: nome.capitalize() , nomes)
# sobrenomes_processados = map(lambda sobrenome: sobrenome.capitalize(), sobrenomes)

# nomes_completos = map(lambda nome, sobrenome: f'{nome} {sobrenome}', nomes_processados, sobrenomes_processados)

# for nome_completo in nomes_completos:
#     print(f'Nome completo: {nome_completo}')



###############################################################################################################################################################

#########8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

#     Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

# Para teste, utilize as seguintes listas de gols marcados e sofridos:

# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]

# Provável texto exibido:

# "A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]

# def calcula_pontos(gols_marcados: int = 0, gols_sofridos: int = 0) -> int, float:
# '''Funcao que calcula os pontos de um time de acordo com a quantidade de gols marcados nas partidas

#     gols_marcados: int, default 0
#         inteiro com a quantidade de gols marcados
#     gols_sofridos: int, default 0
#         inteiro com a quantidade de gols sofridos
    
#     return = pontuacao: int, aproveitamento: float
#         pontuacao do time e seu aproveitamento
# '''
#     pontuacao = 0
#     total_jogos = len(gols_marcados)
    
#     for i in range(total_jogos):
#         if gols_marcados[i]>gols_marcados[i]:
#             pontuacao += 3
#         elif gols_marcados[i]==gols_sofridos[i]:
#             pontuacao += 1
    
#     pontos_maximos = total_jogos * 3    
#     aproveitamento = (pontuacao / pontos_maximos) * 100

#     return pontuacao, aproveitamento

# pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)

# print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aprov:.1f}%")





###############################################################################################################################################################

#########9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

# "Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

# cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
# passeio_alimentacao = [200, 400, 250, 300]
# distancia_de_Recife = [850, 800, 300, 550]

# def gasto_hotel(dias:int = 0) -> float:
#     '''Funcao que calcula os gasto com hotel baseado nos dias de viagem

#         dias: int, default 0
#             inteiro com a quantidade de dias da viagem
        
#         return = gastos: float
#             gastos com hotel
#     '''
#     gasto = dias * 150.00
#     return gasto

# def gasto_gasolina(cidade: str = '') -> float:
#     '''Funcao que calcula os gastos com gasolina baseado na cidade destino

#         cidade: str, default ''
#             nome da cidade de destino
        
#         return = gastos: float
#             gastos com gasolina
#     '''
#     indice = cidades.index(cidade)
#     distancia = distancia_de_Recife[indice]
#     distancia *= 2 #ida e volta
#     litros = distancia / 14
#     gastos = litros * 5
#     return gastos

# def gasto_passeio(cidade: str = '', dias: int = 0) -> float:
#     '''Funcao que calcula os gastos com passeio e alimentacao

#         cidade: str, default ''
#             nome da cidade destino
#         dias: int, default 0
#             quantidade de dias da viagem
        
#         return = gastos: float
#             gastos com passeio e alimentacao
#     '''
#     indice = cidades.index(cidade)
#     gasto_diario = passeio_alimentacao[indice]
#     gastos = gasto_diario * dias
#     return gastos

# cidade = 'Salvador'
# dias = 3
# gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)

# print(f'Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {gastos:.2f} reais')


###############################################################################################################################################################

#########10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

#     Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

# Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.

# frase = input('Digite uma frase: ')

# for pontuacao in [',', '.', '!','?']:
#     frase = frase.replace(pontuacao, ' ')

# palavras_grandes = list(filter(lambda palavra: len(palavra)>= 5, frase.split()))

# print(f"Palavras com 5 ou mais caracteres: {palavras_grandes}")




###############################################################################################################################################################