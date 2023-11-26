#metodo area y metodo perimetro

class cuadrado:
	
	#se crea el constructor, se inicializa el valor del lado =0 para que Python pueda iniciar el procedimiento
	def __init__(self, lado = 0):
		self._lado = lado
	# se crea un metodo que nos permita traer el el atributo privado _lado
	def set_lado(self, lado):
		self._lado = lado
	# Se crea el metodo del area
	def area(self):
		print(f"Hola soy el area:	{self._lado**2} u^2")
	# Se crea el metodo del perimetro entre {} estan las operaciones respectivas
	def perimetro(self):
		print(f"Hola soy el perimetro:	{4*self._lado} u")


	
