def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    
    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print ("Hay %d %s." % (contador, x))


if __name__ == "__main__":
    contar_vocales("murcielago")
