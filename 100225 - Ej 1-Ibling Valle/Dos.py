def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Ingrese un número: "))
    if primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
except ValueError:
    print("Ingrese un número entero.")