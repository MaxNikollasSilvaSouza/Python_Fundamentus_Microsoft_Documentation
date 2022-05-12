from os import error


def process_numbers(entrada):
    lista = []
    try:
        if type(entrada) == list:
            
            for arg in entrada:
                try:
                    conversao = int(arg)
                except ValueError:
                    None
                if type(conversao) == int:
                    lista.append(conversao)
                    conversao = None
            lista.sort()
            return lista
    except ValueError:
       
        return lista

def process_names(entrada):
    lista = []
    try:
        if type(entrada) == list:
           
            for arg in entrada:
                try:
                    conversao = int(arg)
                    None
                except ValueError:
                    if type(arg) == str and arg.isnumeric() == False:
                        lista.append(arg)
                        conversao = None
                
            lista.sort()
            return lista

    except error:
        
        return lista

    