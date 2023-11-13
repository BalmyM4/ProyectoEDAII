from datetime import datetime

def dias_transcurridos(fecha1, fecha2, formato="%d/%m/%y"):
    try:
        # Convertir las fechas de cadena a objetos datetime
        fecha1_obj = datetime.strptime(fecha1, formato)
        fecha2_obj = datetime.strptime(fecha2, formato)

        print(fecha1_obj, " - ", fecha2_obj)

        # Calcular la diferencia entre las fechas
        diferencia = fecha2_obj - fecha1_obj

        # Obtener la cantidad de días
        dias_transcurridos = diferencia.days

        return dias_transcurridos

    except ValueError:
        print("Formato de fecha incorrecto. Utiliza el formato dd/mm/aa.")
        return None

# Ejemplo de uso
fecha_inicial = "01/01/21"
fecha_final = "31/12/23"

dias = dias_transcurridos(fecha_inicial, fecha_final)

if dias is not None:
    print(f"La cantidad de días transcurridos entre {fecha_inicial} y {fecha_final} es: {dias} días.")
