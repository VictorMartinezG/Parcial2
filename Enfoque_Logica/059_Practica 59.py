# Implementación simple de Inducción Gramatical (inferir reglas de secuencias)
import numpy as np

# Conjunto de ejemplos positivos (cadenas que cumplen con la gramática)
positive_examples = [
    "ab", "abc", "abcd", "abcde"
]

# Conjunto de ejemplos negativos (cadenas que no cumplen con la gramática)
negative_examples = [
    "a", "abcdeabc", "xyz", "bcde"
]

# Función para generar la regla más simple (por ejemplo, cadenas que comienzan con 'a' y siguen con 'b', 'c', etc.)
def induce_grammar(positive_examples):
    # Intentamos encontrar un patrón común
    prefix = ""
    for example in positive_examples:
        for i, char in enumerate(example):
            if prefix == "" or example[:i+1] == prefix:
                prefix = example[:i+1]
            else:
                break
    return prefix

# Inducir la gramática desde los ejemplos positivos
generated_rule = induce_grammar(positive_examples)

# Verificar si los ejemplos negativos cumplen con la regla generada
print(f"Regla generada: {generated_rule}")

# Comprobar ejemplos positivos
for example in positive_examples:
    if example.startswith(generated_rule):
        print(f"{example} es un ejemplo válido.")
    else:
        print(f"{example} no cumple con la regla generada.")

# Comprobar ejemplos negativos
for example in negative_examples:
    if example.startswith(generated_rule):
        print(f"{example} no debería ser un ejemplo válido.")
    else:
        print(f"{example} no cumple con la regla generada correctamente.")
