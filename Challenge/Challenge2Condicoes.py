    #Pergunta se a pessoa deseja continuar 
print("Would you like to continue ? (y or yes | n or no)")
answer = input()

    #Caso a pessoa não queira continuar a execeção do programa é interrompida
if answer == 'n' or answer == 'no':
    print("\nExiting")
    #Casi a pessoa deseje continuar , o programa carrega exibe a mensagem e encerra
elif answer == 'y' or answer == 'yes':
    print("\nContinuing...")
    print("\nComplete!")

    #Caso outra coisa seja inserida no input, é exibida essa mensagem.
else:
    print("Please try again and respond with yes or no.")
