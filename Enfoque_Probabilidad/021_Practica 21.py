# TEMA: Naïve Bayes
# OBJETIVO: Clasificar si un email es SPAM o NO-SPAM basado en palabras

# Datos: probabilidad de cada palabra dada una clase
P_palabras_dado_spam = {"oferta": 0.9, "gratis": 0.8}
P_palabras_dado_no = {"oferta": 0.2, "gratis": 0.1}

# Probabilidades previas
P_spam = 0.4
P_no = 0.6

# Observación: ["oferta", "gratis"]
# Suponemos independencia entre palabras (Naïve)

# Probabilidad de ser SPAM
P_spam_total = P_spam * P_palabras_dado_spam["oferta"] * P_palabras_dado_spam["gratis"]

# Probabilidad de ser NO-SPAM
P_no_total = P_no * P_palabras_dado_no["oferta"] * P_palabras_dado_no["gratis"]

# Normalización
normalizador = P_spam_total + P_no_total
P_spam_final = P_spam_total / normalizador

print(f"Probabilidad de ser SPAM: {P_spam_final:.2f}")
