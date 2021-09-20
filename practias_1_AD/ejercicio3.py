def filtrar_palabras(lista, n):
    for i in lista:
        if len(i) > n:
            print(i)

if __name__== "__main__":
    lista=("hola","comida","lideres")
    filtrar_palabras(lista,5)