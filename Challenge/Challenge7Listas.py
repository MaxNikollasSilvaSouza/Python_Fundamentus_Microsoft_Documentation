#Realiza as importações importantes
from itertools import count
import random

#Cria as listas
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []
deck_user = []

#cria um novo deck misturando as duas listas
for  suit in suits:
  for rank in ranks:      
    deck.append(f'{rank} of {suit}')  

#informa o usuário quantas cartas existem no baralho e em seguida seleciona 5 aleatóriamente
#para o usuário
print(f'\nExistem {len(deck)} cartas no baralho.\n\n')
deck_user = random.choices(deck,k=5)

#As cartas que foram selecionadas aleatóriamente para o usuário, são removidas do baralho principal.
for pegou in deck_user:
    for tirar in deck:
        if pegou == tirar:

            #Comparar as cartas visualmente (apresentando)
           # print(f'\n\npegou {pegou}\n')
           # print(f'tirar {tirar}\n\n')
            deck.remove(tirar)
#for card in deck_user:
 #   print(card)

 #Uma outra forma otimizada de realizar o laço acima é usando o laço while assim como segue abaixo
 
 #while len(deck) < 5:
  #  card = random.choice(deck)
   # deck.remove(card)
    #deck_user.append(card)

#Esta linha abaixo foi exigida no exercicio antes da apresentação final
print("Dealing...\n")

#É informado quantas cartas tem no baralho principal após o sorteio das cartas do usuário
print(f'\nQuantidade de cartas no baralho: {len(deck)}')

#É informada a quantidade de cartas nas mãos do usuário assim como quais são
print(f'\nQuantidade de cartas nas mãos do jogador: {len(deck_user)}, sendo elas: {deck_user}\n')