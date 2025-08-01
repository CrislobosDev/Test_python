class Verificador:
    def __init__(self, numero):
        self.numero = numero

    def tabla_multiplicar(self):
        resultado = ""
        i = 1
        while i <= 5:
            resultado += (
                str(self.numero) + "x" + str(i) + "=" + str(i * self.numero) + "\n" # Reemplazo (i + self.numero por i * self.numero)
            )
            i += 1
        return resultado

#PRUEBA CON PYTEST

def test_tabla_multiplicar_para_tres(): # Test para verificar la tabla de multiplicar del 3
    verificador = Verificador(3) # Crear una instancia de Verificador con el número 3
    # El resultado esperado para la tabla del 3 hasta el 5
    resultado_esperado = "3x1=3\n3x2=6\n3x3=9\n3x4=12\n3x5=15\n"
    assert verificador.tabla_multiplicar() == resultado_esperado # Verificar que el resultado de tabla_multiplicar es igual al resultado esperado