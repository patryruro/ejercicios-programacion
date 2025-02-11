def ingresar_datos_de_autos (cantidad_de_autos):
    mi_arreglo = []

    for indice in range (1, int(cantidad_de_autos) + 1):
        marca = input("marca:")
        print(marca)
        modelo = input("modelo:")
        print(modelo)
        color = input("color:")
        print(color)
        ano = input("ano:")
        print(ano)
        mi_diccionario = {"marca":marca,"modelo":modelo,"color":color,"ano":ano}
        mi_arreglo.append(mi_diccionario)
    return mi_arreglo
    
def obtener_nuevo_numero_de_autos():
    cantidad_de_autos=input("ingrese cantidad de autos")
    return cantidad_de_autos

mi_nuevo_numero_de_autos=obtener_nuevo_numero_de_autos()
ingresar_datos_de_autos(mi_nuevo_numero_de_autos)
mi_arreglo=ingresar_datos_de_autos()