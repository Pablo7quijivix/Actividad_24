print("primer commit jaja")

def menu():
    print(f"1.Calcular el factorial de un numero")
    print(f"2. Suma de los primeros numeros naturales")
    print(f"3. Calcular el n-ésimo numero de fibonacci")
    print(f"4. Cuantas veces aparece una letra en una palabra")
    print(f"5. Invrtir una cadena de texto")
    print(f"6. Calcular la potencia de un numero (base^exponente)")
    print(f"7. Salir")
    op=input(f"Eliga una opcion (1-7)")
    match op:
        case "1":
            print(f"esperando jaja")

        case "2":
            print(f"esperando jaja x2")

        case "3":
            print(f"esperando jaja x3")

        case "4":
            print(f"esperando por x4")

        case "5":
            print(f"esperando por X5")

        case "6":
            print(f"esperando por x6")

        case "7":
            print(f"Saliendo del sistema................")

        case _:
            print(f"----Opcion no valida, vuelva a intentarlo...")
