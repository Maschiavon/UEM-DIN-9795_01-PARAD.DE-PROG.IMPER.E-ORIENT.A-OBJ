def selectionsort(lista: list):
    count = 0
    for i in range(0, len(lista)-1):
        posicao_maior = 0
        maior = lista[0]
        for j in range(0, len(lista)-i):
            if maior < lista[j]:
                maior = lista[j]
                posicao_maior = j
        if posicao_maior != len(lista)-1-i:
            count += 1
            aux = lista[len(lista) - 1 - i]
            lista[len(lista) - 1 - i] = maior
            lista[posicao_maior] = aux
            print(lista)
    print("count: " + str(count))
    return lista
