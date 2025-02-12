def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Ingrese un número: "))
    if num < 0:
        print("El factorial es incorrecto")
    else:
        print(f"El factorial de {num} es {factorial(num)}")
except ValueError:
    print("Ingrese un número entero")