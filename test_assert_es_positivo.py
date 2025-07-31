class Verificador:
    def __init__(self, numero):
        self.numero = numero

    def es_positivo(self):
        if self.numero > 0: # se corrige el signo de la condición para verificar si es positivo ( antes era numero < 0)
            return True
        else:
            return False


# PRUEBA CON ASSERT
assert (
    Verificador(2).es_positivo() == True
)  # assert es una forma de verificar condiciones
# si la condición es falsa, se lanza un AssertionError
assert Verificador(3).es_positivo() == True
assert Verificador(0).es_positivo() == False
assert Verificador(-2).es_positivo() == False
assert Verificador(-3).es_positivo() == False

print(
    "Todas las pruebas de assert al metodo es_positivo pasaron correctamentee."
)  # mensaje de éxito si todas las pruebas pasan
