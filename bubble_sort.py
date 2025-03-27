def read_file(archivo):
    try: 
        with open(archivo, 'r') as file:
            return file.read()
    except FileNotFoundError: 
        print("El archivo no existe")
    return None 


def write_file(archivo,contenido_txt):
    try: 
        with open(archivo, 'w') as file: 
            file.write(contenido_txt)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
    return None



# imprimire el TXT 
def imprimir_txt(archivo):
    data = read_file(archivo)
    return data

    

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



def count_palabras_total(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO NO")
        return None 
    palabras = contenido.split()  # dividimos el contenido en palabras
    # print(palabras)
    # print(len(palabras))
    return len(palabras)  # devolvemos la cantidad de palabras



def palabras_unicas(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO NO")
        return None
    
    palabras = contenido.split()
    frecuencia = {} # diccionario donde las keys son las palabras y los valores son las frecuencias

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    unicas = [palabra for palabra, conteo in frecuencia.items() if conteo == 1]
    
    return unicas

def palabra_mas_larga(archivo):
    contenido = read_file(archivo)
    if contenido is None:
        print(f"El archivo '{archivo}' NO NO NO")
        return None
    
    palabras = contenido.split()
    if not palabras:
        
        return None
    
    return max(palabras, key=len)



file = "ejemplo.txt"

print("VECES",count_palabra("hola",file))
print("R",count_renglones(file))
print("TP",count_palabras(file))
print("intimidad",ordenAlfabetico(file))
print("total",count_palabras_total(file))
print( "unicas",palabras_unicas(file))
print("mas larga: (la mia)",palabra_mas_larga(file))
#print(imprimir_txt(file))

print(write_file(file, "chupapi"))