votaram = {}
def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Manda embora!')
    else:
        votaram[nome] = True
        print('Deixe votar!')

verifica_eleitor('Tom')
verifica_eleitor('Mike')
verifica_eleitor('Mike')