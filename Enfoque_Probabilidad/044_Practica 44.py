# Tema: Traducción Automática Estadística
# Se simula una traducción palabra por palabra basada en frecuencias

# Tabla de traducción con probabilidades
traducciones = {
    "el": "the",
    "gato": "cat",
    "duerme": "sleeps",
    "perro": "dog",
    "ladra": "barks"
}

# Traducir frase palabra por palabra
def traducir(frase):
    palabras = frase.split()
    traducidas = [traducciones.get(p, p) for p in palabras]
    return ' '.join(traducidas)

# Ejemplo
print("Traducción:", traducir("el gato duerme"))
