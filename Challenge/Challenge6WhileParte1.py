#Importa a biblioteca random 
import random 

#Sorteia um número aleatório entre 1 e 5
numero = random.randint(1,5)
palpite =0
contador = 1

#Solicita o input
print("Bem vindo ao jogo onde você precisa adivinhar o número! \n")

#Estrutura de repetição condicional
while palpite != numero:
    print('\nDigite valores positivos para continuar ou valores negativos para sair: ')
    #Tratativa de erro
    try:
        palpite = int(input())
        #Verifica o palpite juntamente com o número sorteado
        if palpite == numero:
            print(f'\nParabéns, você acertou em {contador} tentativas!')
            break
        
        #Caso o palpite seja inferior a zero, o programa é encerrado
        elif palpite <0:
            exit()

        #Caso o número informado esteja incorreto, é exibida esta mensagem e é contada mais uma tentativa
        else:
            print("\nNúmero errado.")
        
        contador += 1

    #tratativa de erro
    except ValueError:
        print("Insira apenas números inteiros!")

