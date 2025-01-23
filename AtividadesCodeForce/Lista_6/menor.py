def sublista_sem_menor(lista):
    # Encontrar o menor elemento da lista
    menor = min(lista)
    
    # Criar uma nova lista sem o menor elemento
    nova_lista = []
    encontrou_menor = False  # Para remover apenas a primeira ocorrência do menor
    
    for item in lista:
        if item == menor and not encontrou_menor:
            encontrou_menor = True  # Marca que o menor foi encontrado e ignorado
        else:
            nova_lista.append(item)  # Adiciona o item à nova lista
    
    return nova_lista
