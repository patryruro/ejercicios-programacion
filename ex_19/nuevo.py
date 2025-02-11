mi_arreglo = []
mi_usuario = input("cantidad de usuarios:")
for indice in range(3,int(mi_usuario)):
    nombre = input("nombre:")
    print(f"Hola,{nombre} ")
    edad = input("edad :")
    print(f"Tu edad,{edad} ")
    pais = input("pais : ")
    print(f"pais,{pais} ")
    mi_diccionario = {"nombre" : nombre, "edad" : edad, "pais" : pais}
    mi_arreglo.append(mi_diccionario)
print(mi_arreglo)

    








