from nomina import *
from os import system

def main():
    regs = cargar_nomina()
    op = 0
    while True:
        opc = menu()
        match opc:
            case 1: 
                id = input("Digite el ID del empleado: ")
                index = buscar_empleado(id)
                if index != None:
                    imprimir_empleado(index)
                else: 
                    print(f"El empleado con el ID {id} no existe...")
            
            case 2:
                if len(nomina)> 0:
                    for i in range(0, len(nomina)):
                        imprimir_empleado(i)
                else:
                    print("La nomina actual esta vacia")

            case 3:
                agregar_empleado()

            case 4:
                id = input("Digite el ID del empleado: ")
                index = buscar_empleado(id)
                if index != None:
                    actualizar_empleado(index)
                else: 
                    print(f"El empleado con el ID {id} no existe...")

            case 5: 
                id = input("Digite el ID del empleado: ")
                index = buscar_empleado(id)
                if index != None:
                    eliminar_empleado(index)
                else: 
                    print(f"El empleado con el ID {id} no existe...")

            case 6:
                guardar_nomina()

            case 7:
                break
        system("pause")


                

def menu():
    system("cls")
    print("******* OPERACIONES DE NOMINA *******")
    print("1.....................Buscar empleado")
    print("2.....................Imprimir nomina")
    print("3............Registrar nuevo empleado")
    print("4.................Actualizar empleado")
    print("5....................elimiar empleado")
    print("6......................Guardar nomina")
    print("7.......................salir de menu")
    print("*************************************")

    
    for emp in nomina:
        print(f"ID: {emp["id"]}")
        print(f"Nombre: {emp["nombre"]}")
        print(f"Unidad: {emp["unidad"]}")
        print(f"Salario: {emp["salario"]}")
        print(f"Antiguedad: {emp["antiguedad"]}")

main()
