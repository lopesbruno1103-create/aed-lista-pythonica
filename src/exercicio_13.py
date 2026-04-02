def reduzir_lista(lista):
    nova_lista = []
     for i in range(len(lista)):
        if i < 2:
            nova_lista.append(lista[i])
     return nova_lista
