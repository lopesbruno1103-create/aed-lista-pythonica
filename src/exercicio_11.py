def modify_guest_list(lista, antigo, novo):
    for i in range(len(lista)):
        if lista[i] == antigo:
            lista[i] = novo
    
    return lista