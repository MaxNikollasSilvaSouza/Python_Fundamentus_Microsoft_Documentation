#importa um biblioteca necessária
from os import truncate

#Tratativa de erro
try:
    #Solicita os inputs
    print("Calculadora simples!")

    print("Insira o primeiro número: ")
    primeiro = input()

    print("Insira o segundo número: ")
    segundo = input()

    print("Insira a operação que deseja realizar: ")
    operacao = input()

   
    #Verifica se o valor inserido é numérico
    if primeiro.isnumeric() == False and segundo.isnumeric() == False:
        print("Por gentileza, insira um número!")
        exit()
    
    #Converte os valores para float
    primeiro = float(primeiro)
    segundo = float(segundo)


    resultado = 0
    
    #Verifica qual operação o usuário deseja fazer
    if operacao == '+':
        resultado = primeiro + segundo

    elif operacao == '-':
        resultado = primeiro - segundo

    elif operacao == '*':
        resultado = primeiro * segundo

    elif operacao == '/':
        resultado = primeiro / segundo

    elif operacao == '**':
        resultado = primeiro ** segundo

    elif operacao == '%':
        resultado = primeiro % segundo

    else:
        print('Operação não reconhecida.')
        exit()

    #Exibe o resultado da operação com a formatação de string
    print("O resultado da operação de {} {} {} = {}".format(primeiro, operacao,segundo,resultado))

    #Caso o valor inserido seja incorreto, ele exibe esta mensagem e encerra o programa
except ValueError:
    print("Valores inseridos não reconhecidos!")
    exit()