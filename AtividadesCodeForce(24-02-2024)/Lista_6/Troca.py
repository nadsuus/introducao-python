def lista_troca_menor_primeiro(lista):
    menor_indice = lista.index(min(lista))
    if menor_indice == 0:
        return 0
    lista[0], lista[menor_indice] = lista[menor_indice], lista[0]
    return 1
