#teste = 78
#print(type(teste))
#if isinstance(teste,float):
#    print('blz')
#else:
#    print('estranho')

#um try com um except para evitar erros durante a execução do programa caso o usuário insira valores incorretos
try:
    #Mensagem de bem vindo seguido com o pedido de input
    print("Bem vindo ao conversor de temperatura!")
    print('Digite a temperatura em fahrenheit: ')
    fahrenheit = input()
    #Verifica o tipo da variável e realiza a conversão
    if isinstance(float(fahrenheit),float):
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9

    #Apresenta a temperatura para o usuário, usando a formatação de strings
    print("A temperatura convertida para Celsius é: {} °C".format(round(celsius,2)))

#Caso o usuário insira um input incorreto, cairá neste except
except ValueError:
    print("Valor inserido não é válido.")
    exit()

# ------------------------------ Outra forma de resolver: --------------------------------------
#fahrenheit = input('What is the temperature in Fahrenheit?  ')

#if fahrenheit.isnumeric() == False:
#    print('Input is not a number.')
#    exit()

#fahrenheit = int(fahrenheit)

#celsius = int((fahrenheit - 32) * 5/9)
#print('Temperature in celsius is ' + str(celsius))