def read_file(archivo): 
    try: 
        with open(archivo,'r') as file: 
            return file.read()
    except FileNotFoundError:
            print("NO EXISTEEs")
    return None 

def count_palabra(palabra, archivo):
    contenido = read_file(archivo)
    if contenido is not None: 
         print(f"NO NO {archivo} NO NO")
         return None 
    
    contador = 0
    indice = 0
    longitud_palabra = len(palabra)
    
    while indice < len(contenido) - longitud_palabra: 
        if contenido[indice:indice + longitud_palabra] == palabra: 
                contadro += 1
                indice += longitud_palabra
        else: 
             indice += 1
    return contador
