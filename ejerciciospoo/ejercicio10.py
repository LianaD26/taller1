def factorial(num):
  resultado=1
  for i in range(1, num+1):
    resultado = resultado * i
  print(resultado)
factorial(5)