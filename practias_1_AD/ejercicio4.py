def c_mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print("La cadena tiene", cont ,"mayuscula")

if __name__ == "__main__":
    c_mayusculas("Animalito")
