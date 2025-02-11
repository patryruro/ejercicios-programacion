mi_arreglo = []
mi_usuario = input("cantidad de usuarios:")
for indice in range(5, int(mi_usuario)):
    nombre = input("nombre:")
    print(f"Hola,{nombre}")
    edad = input("edad:")    
    print(f"Tu edad,{edad}")  
    pais = input("Pais:") 
    print(f"tu Pais,{pais}")
    color = input("color de ojos:")
    print(f"Tu color de ojos,{color}")
    mi_diccionario = {"nombre" : nombre, "edad" : edad, "pais" : pais, "color de ojos": color}
    mi_arreglo.append(mi_diccionario)
print(mi_arreglo)