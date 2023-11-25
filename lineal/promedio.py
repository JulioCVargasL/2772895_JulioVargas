#Ingresamos por teclado 5 numeros y sacamos el promedio de los numeros pares

print("Ingresa n cantidad de numeros y te dare el promedio de los pares")

cont= 0

div= 0

par= 0

cant= int(input(f"Ingresa la cantidad de Numeros que deseas ingresar: "))

while cont < cant:

	num = int(input(f"Ingresa el {cont + 1} numero: "))
	if (num%2 == 0):
		par = par + num
		cont += 1
		div += 1
	else:
		cont += 1

if div == 0:
	print("\nNo hay numeros pares")
else:
	prom = par / div
	print(f"\nHay {div} numeros pares")
	print(f"\nEl promedio de los pare es {prom}")
	 
