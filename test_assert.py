# CASOS DE PRUEBA PARA VERIFICAR SI UN NÚMERO ES PAR


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


# PRUEBA CON ASSERT
assert Verificador(2).es_par() == True  # assert es una forma de verificar condiciones
# si la condición es falsa, se lanza un AssertionError
assert Verificador(3).es_par() == False
assert Verificador(0).es_par() == True
assert Verificador(-2).es_par() == True
assert Verificador(-3).es_par() == False

print(
    "Todas las pruebas de assert pasaron correctamentee."
)  # mensaje de éxito si todas las pruebas pasan
