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


# PRUEBA MANUAL
numero = int(
    input("Ingrese un número: ")
)  # se solicita al usuario que ingrese un número
verificador = Verificador(
    numero
)  # se crea una instancia de Verificador con el número ingresado
print(
    "¿Es par?", verificador.es_par()
)  # se imprime si el número es par o no True/False
