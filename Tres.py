try:
    limite = int(input("Ingrese 3 números como minimo: "))
    if limite < 3:
        print("Debe ingresar al menos 3 números.")
    else:
        numeros = []
        for i in range(limite):
            num = int(input(f"Ingrese el número {i + 1}: "))
            numeros.append(num)
        
        print(f"El número mayor es: {max(numeros)}")
        print(f"El número menor es: {min(numeros)}")
except ValueError:
    print("Ingrese 3 números como minimo.")
