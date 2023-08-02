def invertir(lista):
    lista_invertida=[]
    for i in range(len(lista)):
        lista_invertida.insert(0, lista[i])
    print(lista_invertida)

invertir([1,2,3,4,5])