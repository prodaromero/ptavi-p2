#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoo

class Calcoohija(calcoo.Calculadora):
	def multiplicacion(self, op1, op2):
		return op1 * op2
	def division(slef, op1, op2):
		if op2 == 0:
			return('No se puede dividir entre 0')
		else:
			return op1 / op2

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	calculadora = Calcoohija()

	if sys.argv[2] == "suma":
		resultado = calculadora.suma(operando1, operando2)
	elif sys.argv[2] == "resta":
		resultado = calculadora.resta(operando1, operando2)
	elif sys.argv[2] == "multiplica":
		resultado = calculadora.multiplicacion(operando1, operando2)
	elif sys.argv[2] == "divide":
		if operando2 == 0:
			sys.exit("No se puede dividir entre 0")
		else:
			resultado = calculadora.division(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')

	print(resultado)
