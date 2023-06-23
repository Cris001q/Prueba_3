import random 

def menu():
            vehiculos = {}
            nombre = input("ingrese su nombre:")
            apellido =input("ingrese su apellido:")
            version = "1.0"
            while true:
                print("\n----menu----")
                print("1.grabar vehiculo")
                print("2.buscar vehiculo")
                print("3.imprimir certificados")
                print("4.Salir")
                opcion = input("seleccione una opcion(1-4):")

                if opcion == "1":
                    grabar_vehiculo(vehiculos)
                elif opcion == "2":
                    buscar_vehiculo(vehiculos)
                elif opcion == "3":
                    imprimir_certificados(vehiculos)
                elif opcion == "4":
                    print("gracias por utilizar el programa.")
                    print("nombre: {} {} " .format(nombre,apellido)) 
                    print("version:"),      
     
def grabar_vehiculo(vehiculos):
    tipo= input("tipo de vehiculo: ")
    patente = input("patente:")
    marca =input("marca:")
    precio = float(input("precio:"))
    multas =[]
    while true:
        opcion = input ("¿agregar multa? (si/no):") 
        if opcion.lower () == "si"
        monto = float(input("monto de la multa:"))
        fecha = input("fecha de la multa:")
        multas.append((monto, fecha))
    else:
        break
    fecha_registro = input("fecha de registro del vehiculo:")
    nombre_dueño = input("nombre del dueño:")
    vehiculos[patente] = {
        "tipo": tipo,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "nombre_dueño": nombre_dueño,
    }
print("vehiculo registrado correctamente.")

def buscar_vehiculo(vehiculos):
    patente = input("ingrese la patente del vehivulo:")
    if patente in vehiculos:
        vehiculo = vehiculos[patente]
        print("informacion del vehiculo:")
        print("tipo:", vehiculo["tipo"])
        print("patente:", patente)
        print("marca:"; vehiculo["marca"])
        print("precio:", vehiculo["precio"])
        print("multas:")
        for monto, fecha in vehiculo ["multas"]:
            print("-monto:",monto)
            print("fecha:",fecha)
            print("fecha de registro:", vehiculo["fecha_registro"])
            else: 
                print("no se encontro ningun vehiculo con la patente buscada")
                def imprimir_certificados(vehiculos):
                    for patente, vehiculo in vehiculos,items():
                        certificado_contaminantes =
                        random.randint(1500,3500)
                        certificado_anotaciones =
                        random.randint(1500,3500)
                        certificado_multas =
                        random.randint(1500,3500)

        print("certificado para el vehiculo con patente", patente)
        print("-certificado de emision de contaminantes", certificado_contaminantes)
        print("-certificado de anotaciones vigentes:", certificado_anotaciones)
        print("-certificado de multas:", certificado_multas)
        print("datos del dueño:")
        print("-nombre:", vehiculo["nombre_dueño"])
        print("-patente del vehiculo:", patente)
        print()

        