class Verificador:  # se define la clase Verificador
    def __init__(self, numero):  # constructor que recibe un número
        self.numero = numero  # se asigna el número a un atributo de la clase

    def es_par(self):  # método para verificar si el número es par
        if (
            self.numero % 2 == 0
        ):  # aca habia un error de logica dado que se usaba % 2 == 1 y es realmente % 2 == 0
            return True  # si es par, retorna True
        else:
            return False  # si no es par, retorna False


# PPRUEBA CON PYTEST
def test_es_par():  # se define la función de prueba
    assert (
        Verificador(2).es_par() == True
    )  # se verifica si el número 3 es par (Deberia mostrar AssertError)
    assert Verificador(3).es_par() == False
    assert Verificador(0).es_par() == True
    assert Verificador(-2).es_par() == True
    assert Verificador(-3).es_par() == False


print(
    "Todas las pruebas de assert pasaron correctamente."
)  # mensaje de éxito si todas las pruebas pasan
