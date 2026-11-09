def pesquisa_binaria(lista,alvo):
    l = 0
    r = len(lista)-1

    while l <= r:
        meio = (l+r)//2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            r = meio - 1
        else:
            l = meio + 1
    return -1

numeros = [1, 3, 5, 7, 9, 11, 13]
print(pesquisa_binaria(numeros, 7))    # 3
print(pesquisa_binaria(numeros, 1))    # 0
print(pesquisa_binaria(numeros, 13))   # 6
print(pesquisa_binaria(numeros, 4))    # -1