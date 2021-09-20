def mayora20 (tup):
    cont = 0
    for i in tup:
        if i > 20:
            cont += 1
    print ("Hay", cont, "numeros mayores a 20")

if __name__ == "__main__":
    lista=(2,6,8,23,23,5,4,2,76)
    mayora20(lista)