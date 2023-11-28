class hexagono:
	def __init__(self,lado,apotema):
		self.lado = lado
		self.apotema = apotema
	def area (self):
		print(f"El area del exagono es: {(6 * self.lado) * self.apotema/2}")
	def perimetro (self):
		print(f"El perimetro del hexagono es de: {6 * self.lado}")
 
