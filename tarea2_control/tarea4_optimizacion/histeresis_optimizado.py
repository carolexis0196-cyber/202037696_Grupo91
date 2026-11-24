# Monitoreo de histéresis en presión hidráulica 
# Nombre: Carolexis Garcia Montiel
UMBRAL_PRESION_BAR = 5.0

historico_presion_bar = [1.2, 3.4, 5.6, 2.1, 4.5] * 3000


def verificar_cambios_histeresis(lectura_actual):
    # Registra la lectura y emite la alerta según el umbral de presión
    # Se agrega la lectura directamente al historial
    historico_presion_bar.append(lectura_actual)

    if lectura_actual > UMBRAL_PRESION_BAR:
        print("Presion alta")
    else:
        print("Presion estable")
