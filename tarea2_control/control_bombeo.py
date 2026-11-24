# ESCENARIO 3: Sistema de Bombeo Hidroeléctrico
# Sensor de Nivel ultrasónico Microsonic
# Nombre: Carolexis Garcia Montiel
nivel = 10
monitoreo = True
lectura = 0
max_lecturas = 50

while monitoreo and lectura < max_lecturas:
    # Lectura del nivel del tanque
    print(f"\nLectura {lectura + 1}: Nivel = {nivel}%")
    # Verificación de falla del sensor
    if nivel == 0 or nivel == 100:
        print("ERROR: Falla de lectura del sensor")
        monitoreo = False
    # Nivel bajo: encender bomba
    elif nivel < 15:
        print("Control: Bomba encendida - Nivel bajo")
        nivel += 5
    # Operación hidráulica normal
    elif nivel >= 15 and nivel <= 85:
        print("Control: Operación hidráulica normal")
        nivel += 2
    # Nivel superior al 85%: apagar bomba
    else:
        print("Control: Bomba apagada - Tanque lleno")
        nivel -= 4
    lectura += 1

if lectura >= max_lecturas and monitoreo:
    print("\nFin de la simulación: límite de lecturas alcanzado.")
