class triangulo:
	def __init__ (self,base,altura,diagonal):
		self.base = base
		self.altura = altura
		self.diagonal = diagonal
	def area(self):
		print(f"EL area del triangulo rectangulo es: {(self.base * self.altura)/2}")
	def perimetro(self):
		print(f"EL perimetro del tringulo es de: {self.base + self.altura + self.diagonal}") 
