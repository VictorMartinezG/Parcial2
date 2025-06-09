# Tema: Base de Conocimiento
# Este código implementa una base de conocimiento simple con proposiciones

# Creamos una clase para representar una base de conocimiento
class BaseDeConocimiento:
    def __init__(self):
        # Lista que guarda todas las proposiciones
        self.proposiciones = []

    # Método para agregar una proposición a la base
    def agregar(self, proposicion):
        self.proposiciones.append(proposicion)

    # Método para verificar si una proposición está contenida
    def contiene(self, proposicion):
        return proposicion in self.proposiciones

# Creamos una instancia de la base de conocimiento
base = BaseDeConocimiento()

# Agregamos algunas proposiciones
base.agregar("A implica B")
base.agregar("B implica C")

# Verificamos si cierta proposición existe
print("¿Está 'A implica B'? ", base.contiene("A implica B"))
print("¿Está 'C implica A'? ", base.contiene("C implica A"))
