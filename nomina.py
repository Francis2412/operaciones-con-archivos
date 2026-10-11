from os import SEEK_END
from os import SEEK_SET

empleado = {
    "id": "",
    "nombre": "",
    "unidad": "",
    "Salario": 0.0,
    "antiguedad": 0
}

nomina = []

def agregar_empleado():
    print("************** REGISTRO DE EMPLEADO **************")
    empleado["id"] = input("Digite el ID del nuevo empleado: ")
    empleado["nombre"] = input("Digite el nombre del empleado: ")
    empleado["unidad"] = input("Digite la unidad: ")
    empleado["salario"] = float(input("Digite el salario: "))
    empleado["antiguedad"] = int(input("Digite la antiguedad: "))
    nomina.append(empleado.copy())

def buscar_empleado(id:str)->int:
    ''' La fución retorna el índice del empleado en la lista, None si no está'''
    index = None
    for i in range(0, nomina.count):
        if id == nomina[i]["id"]:
            index = i
            break
    return index

def eliminar_empleado(id:str)->bool:
    accion = False 
    index = buscar_empleado(id)
    if index != None:
        nomina.pop(index)
        accion = True
    return accion

def actualizar_empleado(index:str)->bool:
    accion = False
    index = buscar_empleado(id)
    if index != None:
        print("***** ACTUALIZAR EMPLEADO ******")
        print("1........Nombre")
        print("2........Unidad")
        print("3........Salario")
        print("4........Antiguedad")
        print("5........Ninguno")
        opc = int(input("Seleccione la opcion del campo a modificar: "))
        match opc:
            case 1: 
                nomina[index]["nombre"]= input("Digite el nuevo nombre del empleado: ")

            case 2: 
                nomina[index]["unidad"]= input("Digite el nombre del empleado: ")

            case 3:
                nomina[index]["salario"]= float(input("Digite el salario: "))

            case 4:
                nomina[index]["antiguedad"] = int(input("Digite la antiguedad: "))

            case 5:
                print("Ninguno de los campos se ha moficado...")

        accion = True
    return accion

def guardar_nomina():
    fichero = open("Nomina.txt", "a", encoding= "UTP-8")
    for emp in nomina:
        fichero.write(emp["id"])
        fichero.write(emp["nombre"])
        fichero.write(emp["unidad"])
        fichero.writr(str(emp["salario"]))
        fichero.writr(str(emp["antiguedad"]))
    fichero.close()

def cargar_nomina()->int:
    '''La funcion retornar en un numero de registro cargados a la lista 0 -> si no hay registros'''
    cantReg = 0
    fichero = open("Nomina.txt", "r", encoding= "UTF-08")
    # Verificar si el archivo si el archivo tiene datos: 0 bytes -> no tiene
    fichero.seek(0, SEEK_END)
    # Calcular la cantidad de bytes desde el incio hasta el final
    cantBytes = fichero.tell()
    if cantBytes != 0:
        fichero.seek(0, SEEK_SET)
        campo = fichero.readline()
        while campo != "":
            empleado["id"] = campo.rstrip()
            campo = fichero.readline()
            empleado["nombre"] = campo.rstrip()
            campo = fichero.readline()
            empleado["unidad"] = campo.rstrip()
            campo = fichero.readline()
            empleado["unidad"] = campo
            campo = fichero.readline()
            empleado["salario"] = float(campo)
            campo = fichero.readline()
            empleado["antiguedad"] = int(campo)
            nomina.append(empleado.copy())
            campo = fichero.readline()
    fichero.close()
    return cantReg 
 
def imprimir_empleado(index:int):
    print("------------------------")
    print(f"ID: {nomina[index]["id"]}")
    print("------------------------")
    print(f"Unidad: {nomina[index]["unidad"]}")
    print(f"Salario: {nomina[index]["salario"]}")
    print(f"Antiguedad: {nomina[index]["antiguedad"]}")
