#Type Hint
#é uma sintaxe utilizada no Python para indicar o tipo de dado esperado de um parâmetro ou retorno de função, auxiliando na legibilidade e manutenção do código
# def <nome>(<param>: <tipo_param>) -> <tipo_retorno>:
#   <instruções>
#   return resultado

def media(lista: list) -> float:
    calculo = sum(lista) / len(lista)
    return calculo


#Default Value
#é um valor padrão atribuído a um argumento de função que é utilizado caso nenhum valor seja passado pelo usuário.

#   <nome_variavel>: <tipo_variavel> = <valor_variavel>

def media(lista:list = [0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo


#Docstring
#é uma string literal usada para documentar módulo, função, classe ou método em Python. Ela é colocada como o primeiro item de definição e pode ser acessada usando a função help().

# O Docstring deve descrever propósito, parâmetros, tipo de retorno e exceções levantadas pela função. É uma boa prática de programação utilizar Docstrings em seu código para facilitar a leitura, manutenção e compartilhamento do código com outras pessoas desenvolvedoras.

# def <nome>(<param_1>, <param_2>, ..., <param_n>):
#     ''' Texto documentando sua função...
#     '''
#   <instruções>
#   return resultado

def media(lista:list = [0]) -> float:
    '''Função para calcular a média de notas passadas por uma lista

    lista: list, default [0]
        lista com as notas para calcular a média
    return = calculo: float
        média calculada
    '''
    calculo = sum(lista) / len(lista)
    return calculo

help(media)