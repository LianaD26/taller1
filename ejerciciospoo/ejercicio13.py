def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multp = num1 * num2

    print("suma: ", suma)
    print("resta: ", resta)
    print("multiplicación: ", multp)
    if num2 != 0:
        div = num1 / num2
        print("división: ", div)
    else:
        print("No es posible la división por cero")
operaciones(2,6)