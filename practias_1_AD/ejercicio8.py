def main():
    x = int(input ("Cuantos nombres quieres ingresar?: "))
    lista = []
    for i in range(x):
        a = input ("Ingresa el nombre: ")
        lista.append (a)
    
    print ("")
    comienzo = input ("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

if __name__ == "__main__":
    print(main())