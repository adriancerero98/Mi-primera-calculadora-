from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\nCalculadora:")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada de N números")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            try:
                print(f"Resultado: {dividir(a, b)}")
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")
        elif opcion == "5":
            numeros = list(map(float, input("Ingresa los números separados por espacio: ").split()))
            print(f"Resultado: {suma_avanzada(numeros)}")
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
