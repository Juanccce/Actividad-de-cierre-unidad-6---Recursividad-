
# 1) Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 2) Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3) Potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Decimal a Binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de Dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7) Contar Bloques (Pirámide)
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar Dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Menú principal
def menu():
    while True:
        print("\n=== MENÚ DE EJERCICIOS RECURSIVOS ===")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Potencia")
        print("4. Decimal a Binario")
        print("5. Palíndromo")
        print("6. Suma de Dígitos")
        print("7. Contar Bloques (Pirámide)")
        print("8. Contar Dígito")
        print("9. Salir")

        opcion = input("Elegí una opción (1-9): ")

        if opcion == "1":
            num = int(input("Hasta qué número? "))
            for i in range(1, num + 1):
                print(f"{i}! = {factorial(i)}")
        elif opcion == "2":
            pos = int(input("Posición máxima de la serie: "))
            for i in range(pos + 1):
                print(f"F({i}) = {fibonacci(i)}")
        elif opcion == "3":
            base = int(input("Base: "))
            exponente = int(input("Exponente: "))
            print(f"{base}^{exponente} = {potencia(base, exponente)}")
        elif opcion == "4":
            numero = int(input("Número decimal: "))
            binario = decimal_a_binario(numero)
            print(f"Binario: {binario if binario else '0'}")
        elif opcion == "5":
            palabra = input("Palabra sin espacios ni tildes: ").lower()
            print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")
        elif opcion == "6":
            numero = int(input("Número: "))
            print(f"Suma de dígitos: {suma_digitos(numero)}")
        elif opcion == "7":
            n = int(input("Bloques en el nivel más bajo: "))
            print(f"Total de bloques: {contar_bloques(n)}")
        elif opcion == "8":
            numero = int(input("Número: "))
            digito = int(input("Dígito a contar (0-9): "))
            print(f"Aparece {contar_digito(numero, digito)} veces")
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

menu()
