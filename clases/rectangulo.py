class rectangulo:
	def __init__(self,base,altura):
		self.base = base
		self.altura = altura
	def area(self):
		print(f"El area de este rectangulo es de: {self.base * self.altura}")
	def perimetro(self):
		print(f"El perimetro del rectangulo es de:{(self.base + self.altura)*2}")
