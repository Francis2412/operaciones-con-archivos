from os import SEEK_END
from os import SEEK_SET

empleado = {"id":"",
            "nombre":"",
            "unidad":"",
            "salario":0.0,
            "antiguedad":0}

nomina = []

def agregar_empleado():
    print("***** REGISTRO DE EMPLEADOS *****")
    empleado["id"]=input("Digite el ID del nuevo empleado: ")
    empleado["nombre"]=input("Digite el nombre: ")
    empleado["unidad"]=input("Digite la unidad: ")
    empleado["salario"]=float(input("Digite el salario: "))   
    empleado["antiguedad"]=int(input("Digite la antigüedad: "))
    nomina.append(empleado.copy())

def buscar_empleado(id:str)->int:
    '''La función retorna el índice del empleado en la lista, None si no está'''
    index = None
    for i in range(0,len(nomina)):
        if id==nomina[i]["id"]:
            index=i
            break
    return index

def eliminar_empleado(index:int)->bool:
    accion=False
    nomina.pop(index)
    accion=True
    return accion

def actualizar_empleado(index:int)->bool:
    accion=False
    opcion=0
    print("***** ACTUALIZAR EMPLEADO *****")
    print("1..........Nombre")
    print("2..........Unidad")
    print("3..........Salario")
    print("4..........Antigüedad")
    print("5..........Ninguno")
    print("******************************")
    opcion=int(input("Seleccione la opción del campo a modificar: "))
    match opcion:
            case 1:
                    nomina[index]["nombre"]=input("Digite el nuevo nombre del empleado: ")
            case 2:
                    nomina[index]["unidad"]=input("Digite la nueva unidad del empleado: ")
            case 3:        
                    nomina[index]["salario"]=float(input("Digite el nuevo salario del empleado: "))
            case 4:
                    nomina[index]["antiguedad"]=int(input("Digite la nueva antiguedad del empleado: "))
            case 5: 
                    print("Ninguno de los campos se ha modificado...")       
    accion=True
    return accion

def guardar_nomina():
    fichero = open("Nomina.txt","a",encoding="UTF-8")
    for emp in nomina:
        fichero.write(emp["id"]+"\n")
        fichero.write(emp["nombre"]+"\n")
        fichero.write(emp["unidad"]+"\n")
        fichero.write(str(emp["salario"])+"\n")
        fichero.write(str(emp["antiguedad"])+"\n")
    fichero.close()

def cargar_nomina()->int:
    '''La función retorna en número de registros cargados a la lista
       0 -> si no hay registros'''
    cantReg=0
    cantBytes=0
    campo=None
    fichero=open("Nomina.txt","r",encoding="UTF-8")
    # verificar si el archivo tiene datos: 0 bytes -> no tiene
    fichero.seek(0,SEEK_END)
    # calcular la cantidad de bytes desde el inicio hasta el final
    cantBytes=fichero.tell()
    if cantBytes!=0:
        fichero.seek(0,SEEK_SET)
        campo=fichero.readline()
        while campo!="":
             empleado["id"]=campo.rstrip()
             campo=fichero.readline()
             empleado["nombre"]=campo.rstrip()
             campo=fichero.readline()
             empleado["unidad"]=campo.rstrip()
             campo=fichero.readline()
             empleado["salario"]=float(campo)
             campo=fichero.readline()
             empleado["antiguedad"]=int(campo)
             nomina.append(empleado.copy())
             cantReg+=1
             campo=fichero.readline()
    fichero.close()
    return cantReg

def imprimir_empleado(index:int):
     print("---------------------------")
     print(f"ID: {nomina[index]["id"]}")
     print("---------------------------")
     print(f"Nombre: {nomina[index]["nombre"]}")
     print(f"Unidad: {nomina[index]["unidad"]}")
     print(f"Salario: {nomina[index]["salario"]}")
     print(f"Antigüedad: {nomina[index]["antiguedad"]}")
     print("---------------------------")

