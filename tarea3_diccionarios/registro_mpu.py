# ESCENARIO 2: SENSOR MPU6050
# NOMBRE COMPLETO: CAROLEXIS GARCIA MONTIEL
# CODIGO: 1124098260
registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_L",
        "bit_mask": 0xE0,
        "sampling_rate": 1000
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}

max_consultas = 5
consultas = 0

print("CONSULTA DE REGISTROS DEL SENSOR MPU6050")

while consultas < max_consultas:
    busqueda = input(
        "\nIngrese la direccion hexadecimal o el nombre del registro: "
    ).strip()

    datos = None
    direccion_encontrada = None

    # Buscar por direccion hexadecimal
    for direccion, informacion in registro_mpu.items():
        if direccion.lower() == busqueda.lower():
            datos = informacion
            direccion_encontrada = direccion
            break

    # Si no encuentra la direccion, buscar por nombre
    if datos is None:
        for direccion, informacion in registro_mpu.items():
            nombre = informacion.get("register_name", "")
            if nombre.lower() == busqueda.lower():
                datos = informacion
                direccion_encontrada = direccion
                break

    # Mostrar el resultado
    if datos is not None:
        print("\nRegistro encontrado")
        print("Direccion:", direccion_encontrada)
        print("Nombre:", datos.get("register_name"))
        print("Mascara hexadecimal:", hex(datos.get("bit_mask")))
        print("Frecuencia de muestreo:", datos.get("sampling_rate"))
    else:
        print("\nError controlado: registro no encontrado.")

    consultas += 1
    print("Consultas realizadas:", consultas, "de", max_consultas)

print("\nPrograma finalizado.")
