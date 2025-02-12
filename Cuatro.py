from collections import Counter

def numrepetido():
    try:
        numeros = [int(input(f"Número {i+1}: ")) for i in range(7)]
        frecuencia = Counter(numeros) 
        max_repetido = max(frecuencia, key=frecuencia.get)
        print(f"El número que más se repite es {max_repetido} con {frecuencia[max_repetido]} veces")
    except ValueError:
        print("Ingresar solo números enteros.")

numrepetido()
