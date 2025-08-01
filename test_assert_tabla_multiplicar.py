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

# PRUEBA CON ASSERT


mi_verificador = Verificador(2) # Crear una instancia de Verificador con el número 2
 

expected_output = "2x1=2\n2x2=4\n2x3=6\n2x4=8\n2x5=10\n" # Definir el resultado esperado para la tabla del 2

# Realizar la aserción
assert mi_verificador.tabla_multiplicar() == expected_output, "La tabla de multiplicar para 2 no es correcta." # Mensaje de error si la aserción falla

print("¡La prueba con assert para la tabla del 2 pasó con éxito!") 