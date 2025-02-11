def miembros_club (mi_usuario):
    mi_arreglo = []
    for indice in range (1, int(mi_usuario)+ 1) :
        nombre = input("nombre:")
        print(f"hola,{nombre}")
        edad = input("edad:")
        print(f"tu edad,{edad}")
        pais = input("pais:")
        print(f"tu pais,{ pais}")
        mi_diccionario={"nombre" : nombre , "edad": edad, "pais" : pais}
        mi_arreglo.append(mi_diccionario)
        print(mi_arreglo)

mi_usuario= input ("cantidad de miembros: ")  
if mi_usuario == 0:
    print("chao") 
else:
    miembros_club (mi_usuario)


