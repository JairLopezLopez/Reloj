
hora_ingresada = input("Ingresa la hora en formato 5:30: ")

def convertir_hora_a_palabras(hora):
    partes = hora.split(':')
    
    hora_entero = int(partes[0])
    minutos_entero = int(partes[1])
    
    palabras = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez",
                "Once", "Doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
                "diecinueve", "veinte", "veintiuno", "veintidos", "veintitres", "veinticuatro"]
    
    for i in range(21, 30):
        palabras.append(palabras[i - 20])

    if minutos_entero == 0:
        return f"{palabras[hora_entero]} en punto"
    elif minutos_entero == 15:
        return f"{palabras[hora_entero]} y cuarto"
    elif minutos_entero == 30:
        return f"Media después de las {palabras[hora_entero]}"
    elif minutos_entero == 45:
        return f"Cuarto para las {palabras[hora_entero + 1]}"
    elif minutos_entero < 30:
        if minutos_entero == 1:
            return f"Un minuto después de las {palabras[hora_entero]}"
        elif minutos_entero == 5:
            return f"Cinco minutos después de las {palabras[hora_entero]}"
        elif minutos_entero > 20:
            return f"{palabras[hora_entero]} y {palabras[minutos_entero - 20]} minutos después de las {palabras[hora_entero]}"
        else:
            return f"{palabras[minutos_entero]} minutos después de las {palabras[hora_entero]}"
    else:
        if minutos_entero == 31:
            return f"Un minuto para las {palabras[hora_entero + 1]}"
        elif minutos_entero == 55:
            return f"Cinco minutos para las {palabras[hora_entero + 1]}"
        elif minutos_entero > 50:
            return f"{palabras[60 - minutos_entero]} minutos para las {palabras[hora_entero + 1]}"
        else:
            return f"{palabras[60 - minutos_entero]} minutos para las {palabras[hora_entero + 1]}"

resultado = convertir_hora_a_palabras(hora_ingresada)
print(resultado)

