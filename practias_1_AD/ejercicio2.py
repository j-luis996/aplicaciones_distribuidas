def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

if __name__== "__main__":
    lista=("1234","fj34j","423r3efwf")
    print(mas_larga(lista))