hora_ingresada = input("Ingresa la hora en formato 5:30: ")

def convertir_hora_a_palabras(hora):
    partes = hora.split(':')
    
    hora_entero = int(partes[0])
    minutos_entero = int(partes[1])
    
    palabras = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez",
                "Once", "Doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
                "diecinueve", "veinte", "veintiuno", "veintidos", "veintitres", "veinticuatro", 
                "Veinticinco", "veintiseis", "veintisiete", "veintiocho", "Veintinueve"]
    
    if hora_entero == 0:
        if minutos_entero == 0:
            return "Media noche"
        else:
            return f"{palabras[minutos_entero]} minutos después de la media noche"
    elif minutos_entero == 0:
        return f"{palabras[hora_entero]} en punto"
    elif minutos_entero == 15:
        return f"{palabras[hora_entero]} y cuarto"
    elif minutos_entero == 30:
        return f"Media después de las {palabras[hora_entero]}"
    elif minutos_entero == 45:
        return f"Cuarto para las {palabras[hora_entero + 1]}"
    elif minutos_entero == 1:
        return f"{palabras[minutos_entero]} minuto después de las {palabras[hora_entero]}"
    elif minutos_entero == 5:
        return f"{palabras[minutos_entero]} minutos después de las {palabras[hora_entero]}"
    elif minutos_entero < 30:
        return f"{palabras[minutos_entero]} minutos después de las {palabras[hora_entero]}"
    else:
        return f"{palabras[60 - minutos_entero]} minutos para las {palabras[hora_entero + 1]}"

resultado = convertir_hora_a_palabras(hora_ingresada)
print(resultado)

