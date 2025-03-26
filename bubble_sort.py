def read_file(archivo):
    try: 
        with open(archivo, 'r') as file:
            return file.read()
    except FileNotFoundError: 
        print("El archivo no existe")
    return None 


def count_palabra(palabra, archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO")
        return None
    
    contador = 0
    indice = 0
    longitud_palabra = len(palabra)
    
    while indice <= len(contenido) - longitud_palabra:
        if contenido[indice:indice + longitud_palabra] == palabra:
            contador += 1
            indice += longitud_palabra  # Saltar al final de la palabra encontrada para evitar solapamientos
        else:
            indice += 1
    
    return contador



            #      for i in range(limite):
            # if contenido[i:i + derivadaD_DX] == palabra:
            #     contador += 1
        
def count_renglones(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO")
        return None
    
    contador = 0
    for caracter in contenido:
        if caracter == '\n':
            contador += 1
    
    # print(contador)
    # print(pruebaDeCero)

    if contenido and contenido[-1] != '\n':
        contador += 1
    
    return contador



def count_palabras(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f" NO {archivo}' NO")
        return None
    
    palabras = set()  
    en_palabra = False
    for caracter in contenido:
        if caracter.isalnum(): # DIEGO ESTO ES UN identificador de caracteres alfanumericos 
            if not en_palabra:
                palabras.add(caracter)  
                en_palabra = True
        else:
            en_palabra = False
    
    return len(palabras)  # Solo ponemos la cantidad de palabras que no se repiten pues por los sets

def ordenAlfabetico(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO NO")
        return None
    
    palabras = set(contenido.split())  # ADIOS A DUPLICADOS
    palabras = sorted(palabras)  # ordenacion
    
    return palabras


file = "ejemplo.txt"

print("VECES",count_palabra("hola",file))
print("R",count_renglones(file))
print("TP",count_palabras(file))
print("intimidad",ordenAlfabetico(file))