def main():
    a_curso = int(input ("Ingresa el anio en curso: "))
    for i  in range (3):
        nombre = input ("Nombre de la persona: ")
        nacimiento = int(input ("Anio de nacimiento: "))
        print  (nombre, "cumple", (a_curso - nacimiento), "anios en el", a_curso)

if __name__ == "__main__":
    main()