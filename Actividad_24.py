def factorial(num):
    if num ==0 or num ==1:#aqui estamos estructurando el caso base
        return 1
    else:
        return num* factorial(num-1)

def SumaNumerosNaturales(n):
    if n <0: # condicional del caso base
        return 1
    else:
        return n + SumaNumerosNaturales(n+1)



def menu():
    print(f"\n----------MENU DE RECURSIVIDAD----------")#funcion del menu (sin parametros y sin retorno)
    print(f"1.Calcular el factorial de un numero")
    print(f"2. Suma de los primeros numeros naturales")
    print(f"3. Calcular el n-ésimo numero de fibonacci")
    print(f"4. Cuantas veces aparece una letra en una palabra")
    print(f"5. Invrtir una cadena de texto")
    print(f"6. Calcular la potencia de un numero (base^exponente)")
    print(f"7. Salir")

while True:
    menu()
    op = input(f"Eliga una opcion (1-7): ")

    match op:
        case "1":
            print(f"\n----------Factorial de un numero------------")
            num = int(input(f"Ingrese un numero para calcular su factorial: "))
            print(f"El factorial de {num} es igual: {factorial(num)}")

        case "2":
            print(f"\n---------Suma de N numeros naturales----------")
            n=int(input(f"Ingrese un numero positivo para suma desde '1' hasta 'n' recursivmente: "))
            print(f"La sumatoria del numero natural: {n}, es igual a: {SumaNumerosNaturales(n)}")

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
            break

        case _:
            print(f"----Opcion no valida, vuelva a intentarlo...")


