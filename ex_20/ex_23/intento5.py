def miembros_club (mi_usuario):
    mi_arreglo = []
    for indice in range (1, int(mi_usuario)+ 1) :
        # print(indice)
        nombre=input("nombre de campos:")
        mi_arreglo.append(nombre)
    return mi_arreglo
    
def crear_diccionario (arreglo_campo):
    diccionario = {}
    for campo in arreglo_campo :
        diccionario[campo] = input(f"ingrese {campo}:")
    
    return diccionario

    
mi_usuario= input ("cantidad de campos: ")  
if mi_usuario == 0:
    print("chao") 
else:
    mi_arreglo = miembros_club(mi_usuario)
    print(crear_diccionario(mi_arreglo))
     
   
    
    
    # for indice in range (1, int(mi_usuario) +1) :
    #     print(indice)
    #     edad=input("edad de campos:")
    #     mi_arreglo.append(edad)
    # mi_usuario=input ("edad de campos: ")
    # print(mi_arreglo)
    # for indice in range (1, int(mi_usuario) +1):
    #     print(indice)
    #     genero=input("genero:")
    #     mi_arreglo.append(genero)
    # mi_usuario=input("genero:") 
    # print(mi_arreglo)


