
#Tenta executar o que está no try, caso algo dê errado, ele vai direto para a "except"
try:

    #Solicita os inputs
    print('Insira a data atual: ')
    data = input()

    print('\nInsira as calorias do café da manhã: ')
    cafe_manha = float(input())

    print('\nInsira as calorias do almoço: ')
    almoco = float(input())

    print("\nInsira as calorias do jantar: ")
    janta = float(input())

    print('\nInsira as calorias dos lanches: ')
    lanches = float(input())

    #realiza o cálculo
    total = str(cafe_manha + almoco + janta + lanches)

    #Exibe o resultado
    print('\n\nTotal de calorias consumidas em ' + data + ': '+ total)

    #Caso o 'try' de erro, ele cai no except onde é exibida a menssagem de erro
except ValueError:
    print("Devido ao que foi inserido incorretamente, não foi possível continuar.") 

