resultados = []

def mostras_resultados():
    for item in resultados:
        print(item)
    mostrar_menu()


def area_cuadrado():
    lado=input('lado del cuadrado')
    lado=int(lado)
    a=lado*lado
    resultados.append(f'Area de un cuadra  {a}')
    print(a)


def area_rectangulo():
    base=input('Base del Rectangulo: ')
    altura=input('Altura del Rectangulo: ')
    base=float(base)
    altura=float(altura)
    a=base*altura
    resultados.append(f'Area de un rect  {a}')
    print(a)

def area_triangulo():
    base=input('Base del Triangulo: ')
    altura=input('Altura del Triangulo: ')
    base=float(base)
    altura=float(altura)
    a= (base*altura)/ 2
    print(a)

    mostrar_menu()

def mostrar_menu():
    print('1.- area cuadrado')
    print('2.- area rectangulo')
    print('3.- area triangulo')
    print('4.- area circulo')
    opcion=input('opcion')
    opcion=int(opcion)

    if opcion == 1:
        area_cuadrado()
        mostrar_menu()
    elif opcion == 2:
        area_rectangulo()
        mostrar_menu()
    elif opcion == 3:
        area_triangulo()
    else:
        print("Opcion no Valida")


# Iniciar programa
mostrar_menu()
