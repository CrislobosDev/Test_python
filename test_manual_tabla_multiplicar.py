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

# PRUEBA MANUAL

tabla_cinco = Verificador(5)
print(tabla_cinco.tabla_multiplicar())

# Salida esperada:
# 5x1=5
# 5x2=10
# 5x3=15        
# 5x4=20
# 5x5=25