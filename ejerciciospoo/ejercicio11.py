#Crear un programa que genere una lista de números pares entre 1 y 100
def pares():
    lista_pares=[]
    for i in range(101):
        if i % 2==0:
            lista_pares.append(i)
        else:
            continue
    print(lista_pares)
pares()
