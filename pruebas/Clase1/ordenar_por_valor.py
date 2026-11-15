# Ejercicio de pruebas
#Escribe desde cero la función ordenar_por_valor(pares: dict) -> dict, que reciba un diccionario y devuelva otro con los mismos pares ordenados de mayor a menor valor.
#Ejemplo: {"web01": 45, "sql01": 92, "app01": 70} → {"sql01": 92, "app01": 70, "web01": 45}

def ordenar_por_valor(pares: dict) -> dict:
    # Ordenar el diccionario por valor de mayor a menor
    return dict(sorted(pares.items(), key=lambda item: item[1], reverse=True))

Diccionario = {"web01": 45, "sql01": 92, "app01": 70}
Diccionario_ordenado = ordenar_por_valor(Diccionario)
print(Diccionario_ordenado)  # Salida: {'sql01': 92, 'app01': 70, 'web01': 45}