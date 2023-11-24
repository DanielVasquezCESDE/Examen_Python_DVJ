
print(f"\nCalcule el factorial del valor que ingrese\n")

numero = int(input("\nIngrese al número al que se le va a calcular el factorial\n"))

Calcular_Factorial = lambda n: n*Calcular_Factorial(n-1) if n>1 else True

funcion = Calcular_Factorial(numero)

print(funcion)