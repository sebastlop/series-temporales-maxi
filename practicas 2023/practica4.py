def formatear_problemas_aritmeticos(problemas, mostrar_respuestas=False):
    longitud_maxima = max(len(problema) for problema in problemas)
    resultado = []
    respuestas = []
    
    for problema in problemas:
        operandos = problema.split()
        operador = operandos[1]
        problema_linea = f"{operandos[0].rjust(longitud_maxima)}\n{operador + ' ' + operandos[2].rjust(longitud_maxima - len(operador) - 1)}\n{'-' * longitud_maxima}"
        resultado.append(problema_linea)
        
        if mostrar_respuestas:
            resultado_evaluado = eval(problema.replace('=', ''))  # Evalúa la expresión para obtener la respuesta
            respuesta_linea = str(resultado_evaluado).rjust(longitud_maxima)
            respuestas.append(respuesta_linea)
    
    resultado.extend(respuestas)  # Agrega las respuestas debajo de los problemas si es necesario
    return "\n".join(resultado)

# Ejemplo de uso
problemas = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
mostrar_respuestas = True

resultado_formateado = formatear_problemas_aritmeticos(problemas, mostrar_respuestas)
print(resultado_formateado)
