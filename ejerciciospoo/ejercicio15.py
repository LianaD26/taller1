def palindromo(cadena):
    cadena_invertida = []
    for i in range(len(cadena)):
        cadena_invertida.insert(0, cadena[i])
    if list(cadena) == cadena_invertida:
        print("palidrome")
    else:
        print("no es palindrome")

palindromo("liana")