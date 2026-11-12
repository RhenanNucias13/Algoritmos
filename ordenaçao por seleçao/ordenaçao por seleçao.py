def achar_menor(lista):
    menor = lista[0]
    menor_indice = 0

    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(lista):
    novalista = []
    for i in range(len(lista)):
        menor_indice = achar_menor(lista)
        novalista.append(lista.pop(menor_indice))
    return novalista

print(ordenacao_por_selecao([5, 3, 6, 2, 10]))   # [2, 3, 5, 6, 10]
print(ordenacao_por_selecao([]))                  # []
print(ordenacao_por_selecao([1]))                 # [1]
print(ordenacao_por_selecao([4, 4, 1]))           # [1, 4, 4]