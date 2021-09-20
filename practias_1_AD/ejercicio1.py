def max_in_list(lista):
    inicio = 0
    for i in lista:
        if i > inicio:
            inicio = i
    return inicio

if __name__== "__main__":
    lista=(16,2,8,4,5,6)
    print(max_in_list(lista))