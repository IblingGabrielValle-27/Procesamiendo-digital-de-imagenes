def palindromo(cadena):
    cadena_limpia = ''.join(cadena.lower().split())
    return cadena_limpia == cadena_limpia[::-1]

try:
    texto = input("Ingrese una palabra: ")
    if palindromo(texto):
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")
except Exception as e:
    print(f"Existe un error: {e}")