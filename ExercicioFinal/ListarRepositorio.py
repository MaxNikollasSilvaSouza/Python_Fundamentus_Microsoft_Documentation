import requests
import json

class listaDeRepositorios():

    #é a função de inicio do programa, o 'self' é semelhante a um dicionário em python, armazena variáveis na própria classe
    def __init__(self,usuario):
        self._usuario = usuario

    #realiza a requisição
    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    
    #imprime a lista de repositórios
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)