class circulo:

	pi=3.1416

	def __init__(self,radio):
		self.radio = radio
	def area(self):
		print(f"El area es de: {circulo.pi*self.radio**2}")
	def perimetro(self):
		print(f"El perimetro es de: {2*circulo.pi*self.radio}")
