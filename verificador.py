# archivo: verificador.py
class Verificador:
    def __init__(self, numero):
        self.numero = numero

    def es_par(self):
        if self.numero % 2 == 1:
            return True
        else:
            return False

    def es_positivo(self):
        if self.numero < 0:
            return True
        else:
            return False

    def tabla_multiplicar(self):
        resultado = ""
        i = 1
        while i <= 5:
            resultado += (
                str(self.numero) + "x" + str(i) + "=" + str(i + self.numero) + "\n"
            )
            i += 1
        return resultado
