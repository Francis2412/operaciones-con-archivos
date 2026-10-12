from os import SEEK_END, SEEK_SET

empleado = {
    "id": "",
    "nombre": "",
    "unidad": "",
    "salario": 0.0,
    "antiguedad": 0
}

nomina = []

def agregar_empleado():
    print("***** REGISTRO DE EMPLEADOS *****")

    id = input("Digite el ID del nuevo empleado: ").strip()

    if id == "":
        print("El ID no puede estar vacio.")
        return

    if buscar_empleado(id) is not None:
        print("Ya existe un empleado con ese ID.")
        return

    nombre = input("Digite el nombre: ").strip()
    unidad = input("Digite la unidad: ").strip()

    try:
        salario = float(input("Digite el salario: "))
        antiguedad = int(input("Digite la antiguedad: "))

        if salario < 0 or antiguedad < 0:
            print("El salario y la antiguedad no pueden ser negativos.")
            return

    except ValueError:
        print("Error: el salario debe ser numerico y la antiguedad un entero.")
        return

    empleado["id"] = id
    empleado["nombre"] = nombre
    empleado["unidad"] = unidad
    empleado["salario"] = salario
    empleado["antiguedad"] = antiguedad

    nomina.append(empleado.copy())
    print("Empleado registrado correctamente.")

def buscar_empleado(id: str) -> int:
    """Retorna el indice del empleado o None si no existe."""
    for i in range(len(nomina)):
        if id == nomina[i]["id"]:
            return i

    return None

def eliminar_empleado(index: int) -> bool:
    if 0 <= index < len(nomina):
        nomina.pop(index)
        return True

    return False

def actualizar_empleado(index: int) -> bool:
    if not 0 <= index < len(nomina):
        print("Indice de empleado no valido.")
        return False

    print("***** ACTUALIZAR EMPLEADO *****")
    print("1..........Nombre")
    print("2..........Unidad")
    print("3..........Salario")
    print("4..........Antiguedad")
    print("5..........Ninguno")
    print("******************************")

    try:
        opcion = int(input("Seleccione la opcion del campo a modificar: "))
    except ValueError:
        print("Debe ingresar un numero.")
        return False

    match opcion:
        case 1:
            nombre = input("Digite el nuevo nombre del empleado: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacio.")
                return False
            nomina[index]["nombre"] = nombre

        case 2:
            unidad = input("Digite la nueva unidad del empleado: ").strip()
            if unidad == "":
                print("La unidad no puede estar vacia.")
                return False
            nomina[index]["unidad"] = unidad

        case 3:
            try:
                salario = float(input("Digite el nuevo salario del empleado: "))
                if salario < 0:
                    print("El salario no puede ser negativo.")
                    return False
                nomina[index]["salario"] = salario
            except ValueError:
                print("El salario debe ser numerico.")
                return False

        case 4:
            try:
                antiguedad = int(input("Digite la nueva antiguedad del empleado: "))
                if antiguedad < 0:
                    print("La antiguedad no puede ser negativa.")
                    return False
                nomina[index]["antiguedad"] = antiguedad
            except ValueError:
                print("La antiguedad debe ser un numero entero.")
                return False

        case 5:
            print("Ningun campo ha sido modificado.")
            return False

        case _:
            print("Opcion no valida.")
            return False

    print("Empleado actualizado correctamente.")
    return True


def guardar_nomina():
    try:
        with open("Nomina.txt", "w", encoding="UTF-8") as fichero:
            for emp in nomina:
                fichero.write(emp["id"] + "\n")
                fichero.write(emp["nombre"] + "\n")
                fichero.write(emp["unidad"] + "\n")
                fichero.write(str(emp["salario"]) + "\n")
                fichero.write(str(emp["antiguedad"]) + "\n")

        print("Nomina guardada correctamente.")

    except OSError as error:
        print(f"No se pudo guardar la nomina: {error}")

def cargar_nomina() -> int:
    """Carga los empleados del archivo y retorna la cantidad cargada."""
    cantReg = 0
    nomina.clear()

    try:
        with open("Nomina.txt", "r", encoding="UTF-8") as fichero:
            fichero.seek(0, SEEK_END)
            cantBytes = fichero.tell()

            if cantBytes == 0:
                return 0

            fichero.seek(0, SEEK_SET)
            lineas = fichero.readlines()

    except FileNotFoundError:
        return 0
    except OSError as error:
        print(f"No se pudo leer la nomina: {error}")
        return 0

    if len(lineas) % 5 != 0:
        print("Advertencia: el archivo contiene un registro incompleto.")

    for i in range(0, len(lineas) - 4, 5):
        try:
            id = lineas[i].strip()
            nombre = lineas[i + 1].strip()
            unidad = lineas[i + 2].strip()
            salario = float(lineas[i + 3].strip())
            antiguedad = int(lineas[i + 4].strip())

            if id == "" or salario < 0 or antiguedad < 0:
                print(f"Registro invalido en la linea {i + 1}. Se omitira.")
                continue

            if buscar_empleado(id) is not None:
                print(f"ID duplicado {id}. Se omitira ese registro.")
                continue

            empleado["id"] = id
            empleado["nombre"] = nombre
            empleado["unidad"] = unidad
            empleado["salario"] = salario
            empleado["antiguedad"] = antiguedad

            nomina.append(empleado.copy())
            cantReg += 1

        except ValueError:
            print(f"Datos invalidos en el registro de la linea {i + 1}. Se omitira.")

    return cantReg

def imprimir_empleado(index: int):
    if not 0 <= index < len(nomina):
        print("Indice de empleado no valido.")
        return

    print("---------------------------")
    print(f"ID: {nomina[index]['id']}")
    print(f"Nombre: {nomina[index]['nombre']}")
    print(f"Unidad: {nomina[index]['unidad']}")
    print(f"Salario: {nomina[index]['salario']}")
    print(f"Antiguedad: {nomina[index]['antiguedad']}")
    print("---------------------------")
