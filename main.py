from nomina import *
from os import system

def main():
    regs = cargar_nomina()
    print(f"Registros cargados: {regs}")

    while True:
        try:
            opc = menu()
        except ValueError:
            print("Debe ingresar un numero.")
            system("pause")
            continue

        match opc:
            case 1:
                id = input("Digite el ID del empleado: ").strip()
                index = buscar_empleado(id)

                if index is not None:
                    imprimir_empleado(index)
                else:
                    print(f"El empleado con ID {id} no existe...")

            case 2:
                if len(nomina) > 0:
                    print("********** NOMINA EMPRESARIAL **********")

                    for i in range(len(nomina)):
                        imprimir_empleado(i)
                else:
                    print("La nomina actual esta vacia.")

            case 3:
                agregar_empleado()

            case 4:
                id = input("Digite el ID del empleado: ").strip()
                index = buscar_empleado(id)

                if index is not None:
                    actualizar_empleado(index)
                else:
                    print(f"El empleado con ID {id} no existe...")

            case 5:
                id = input("Digite el ID del empleado: ").strip()
                index = buscar_empleado(id)

                if index is not None:
                    if eliminar_empleado(index):
                        print("Empleado eliminado correctamente.")
                else:
                    print(f"El empleado con ID {id} no existe...")

            case 6:
                guardar_nomina()

            case 7:
                confirmar = input(
                    "Desea guardar los cambios antes de salir? (s/n): "
                ).strip().lower()

                if confirmar == "s":
                    guardar_nomina()

                print("Saliendo del programa...")
                break

            case _:
                print("Opcion no valida.")

        system("pause")

def menu() -> int:
    system("cls")
    print("****** OPERACIONES DE NOMINA ******")
    print("1............Buscar empleado")
    print("2............Imprimir nomina")
    print("3............Registrar nuevo empleado")
    print("4............Actualizar empleado")
    print("5............Eliminar empleado")
    print("6............Guardar nomina")
    print("7............Salir del menu")
    print("***********************************")

    return int(input("Seleccione una opcion: "))

if __name__ == "__main__":
    main()
