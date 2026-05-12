def odd_numbers(n):
    lista = []
    
    for i in range(1, n + 1):
        if i % 2 != 0:
            lista.append(i)
    
    return lista