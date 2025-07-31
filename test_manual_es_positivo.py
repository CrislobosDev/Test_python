class Verificador:
    def __init__(self, numero):
        self.numero = numero

    def es_positivo(self):
        if self.numero > 0: # se corrige el signo de la condición para verificar si es positivo ( antes era numero < 0)
            return True
        else:
            return False


# PRUEBA MANUAL
numero = int(
    input("Ingrese un número: ")
)  # se solicita al usuario que ingrese un número
verificador = Verificador(
    numero
)  # se crea una instancia de Verificador con el número ingresado
print(
    "¿Es positivo?", verificador.es_positivo()
)  # se imprime si el número es par o no True/False
