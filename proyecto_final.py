import os

print("")
print("**********************************************************")
print("Bienvenidos al sistema de historias clinicas del hospital.")
print("**********************************************************")


# **********************
# * VARIABLES GLOBALES *
# **********************
running = True
database = list()

# **********************
# * FUNCIONES GLOBALES *
# **********************
def show_menu():
    print("")
    print("\t\t 1- Cargar paciente")
    print("\t\t 2- Buscar paciente")
    print("\t\t 3- Listar pacientes")
    print("\t\t 4- Salir")
    print("")
    res = input("INGRESE UNA OPCIÓN --> ")
    os.system("cls")
    return res

def response_validate(r):
    validated = False
    num_res = 0

    if response.isdigit(): #controla si el texto ingresado es un numero
        msg = "Entrada correcta."
        num_res = int(response)
        if num_res > 0 and num_res < 5:
            msg = "Esta en rango."
            validated = True
        else:
            msg = "No esta en rango."
    else:
        msg= "Entrada incorrecta."

    return validated, num_res, msg




# **********************
# * LOOP PRINCIPAL *
# **********************

while running:
    response = show_menu()
    validated, num_res, msg = response_validate(response)
    # print(validated, num_res, msg)
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente.\n")
            history = input("Ingrese el problema del paciente.\n")
            paciente = {"nombre":name , "historia":history}
            database.append(paciente)
            print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente.\n")
            patient = 0
            for x in range(len(database)): # recorre la lista

                if database[x]["nombre"].lower() == name.lower(): # SE PUEDE HACER ASI
                    print("")
                    print("PACIENTE ENCONTRADO | HISTORIA CLINICA -> ", database[x]["historia"])
                    print("")
                else: 
                    patient += 1
            if patient == len(database):
                print("Paciente no encontrado.")


        elif num_res == 3:
            print("***********************")
            print("*LISTADO DE PACIENTES.*")
            print("***********************")
            for x in range(len(database)): # .rjust lo que hace es crear una columna a la derecha, .ljust a la izaquierda, el numero entre parentesis dice el tamaño
                print("Nombre -> ".ljust(10),database[x]["nombre"], "\t\t | Historia clinica ->".ljust(10), database[x]["historia"])
            print("FIN DE LA LISTA.")

        elif num_res == 4:
            running = False

    else:
        print("Opción incorrecta!!!")
        print("")

print("************************")
print("*APLICACION FINALIZADA.*")
print("************************")


        # name = name.lower() # SE PUEDE HACER ASI O






# *************************
# *BUCLE WHILE ALTERNATIVO*
# *************************
# ESTE FUE EL PRIMER BUCLE, FUNCIONA SI QUIERO BUSCAR MAS COSAS QUE LA HISTORIA CLINICA XQ LE PUEDO PONER MAS PRINTS
# COPIANDO EL FORMATO
# EL QUE ESTA ARRIBA ES ESPECIFICO PARA EL PROYECTO.
"""
while running:
    response = show_menu()
    validated, num_res, msg = response_validate(response)
    # print(validated, num_res, msg)
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente.\n")
            history = input("Ingrese el problema del paciente.\n")
            paciente = {"nombre":name , "historia":history}
            database.append(paciente)
            print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente.\n")
            
            for x in range(len(database)): # recorre la lista
                for k, v in database[x].items(): # recorre el diccionario
                    if k == "nombre" and v.lower() == name.lower(): # SE PUEDE HACER ASI
                        print("")
                        print("PACIENTE ENCONTRADO | HISTORIA CLINICA -> ", database[x]["historia"])
                        print("")
                    else:
                        print("Paciente no encontrado.")


        elif num_res == 3:
            print("")

        elif num_res == 4:
            print("")

    else:
        print("")
"""