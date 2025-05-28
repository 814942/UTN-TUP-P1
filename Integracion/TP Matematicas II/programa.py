from TP_Integracion import (
    pedir_dnis,
    suma_dni,
    union,
    interseccion,
    diferencia,
    mostrar_frecuencia,
    nacimientos,
    complemento_U,
    generador_de_conjuntos,
)
# Funcion Main con funciones y opciones
def main():
    dnis = pedir_dnis()

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar frecuencia de dígitos de cada DNI")
        print("2. Mostrar suma de dígitos de cada DNI")
        print("3. Unión de dígitos")
        print("4. Intersección de dígitos")
        print("5. Diferencia (primer DNI - segundo DNI)")
        print("6. Diferencia simétrica (A ∆ B)")
        print("7. Mostrar si hay dígitos fuera del conjunto universal")
        print("8. Operaciones con años de nacimiento")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for dni in dnis:
                mostrar_frecuencia(dni)

        elif opcion == "2":
            for dni in dnis:
                print(f"Suma de dígitos del DNI {dni}: {suma_dni(dni)}")

        elif opcion == "3":
            print("Unión de dígitos:", union(dnis))

        elif opcion == "4":
            print("Intersección de dígitos:", interseccion(dnis))

        elif opcion == "5":
            if len(dnis) >= 2:
                print("Diferencia A - B:", diferencia(dnis))
            else:
                print("Se necesitan al menos dos DNIs para esta operación.")

        elif opcion == "6":
            if len(dnis) >= 2:
                a = set(generador_de_conjuntos(dnis[0]))
                b = set(generador_de_conjuntos(dnis[1]))
                dif_sim = list((a - b).union(b - a))
                print("Diferencia simétrica A ∆ B:", dif_sim)
            else:
                print("Se necesitan al menos dos DNIs para esta operación.")

        elif opcion == "7":
            if complemento_U(dnis):
                print("Hay dígitos que no aparecen en los DNIs (conjunto incompleto).")
            else:
                print("Todos los dígitos del conjunto universal (0 al 9) están representados.")

        elif opcion == "8":
            nacimientos()

        elif opcion == "9":
            print("Gracias por usar el programa. ¡D10S te bendiga!")
            break

        else:
            print("Opción inválida. Intentalo nuevamente.")

if __name__ == "__main__":
    main()
