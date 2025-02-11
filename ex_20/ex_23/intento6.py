def miembros_club(mi_usuario): 
mi_arreglo = []
for indice in range(1, int(mi_usuario) + 1):
        nombre = input(f"Nombre del campo {indice}: ")
        mi_arreglo.append(nombre)
return mi_arreglo



def crear_diccionario (arreglo_campo):
    diccionario = {}
    for campo in arreglo_campo :
        diccionario[campo] = input(f"ingrese {campo}:")
    
    return diccionario

def crear_diccionarios(arreglo_campo, num_personas):
    lista_diccionarios = []
    for persona in range(num_personas):    
        print(f"Datos de la persona {persona + 1}:")
        diccionario= crear_diccionario(arreglo_campo)
        lista_diccionarios.append(diccionario)
    return lista_diccionarios

mi_usuario = input("Cantidad de campos: ")
if int(mi_usuario) == 0:
    print("Chao")
else:
    mi_arreglo = miembros_club(mi_usuario)
    num_personas = int(input("Cantidad de personas: "))
    resultado = crear_diccionarios(mi_arreglo, num_personas)
    print("\nResultado:")
    for i, dic in enumerate(resultado, 1):
        print(f"Persona {i}: {dic}")


  
 

    



