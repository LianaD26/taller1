def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    print("Suma de los elementos de la lista: ", suma)

suma_lista([1,2,3,2])