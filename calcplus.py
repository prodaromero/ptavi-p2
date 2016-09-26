#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija

fichero = open('Operaciones', 'r')

lineas = fichero.readlines()

primera_linea = lineas

calculadora = calcoohija.Calcoohija()

if __name__ == "__main__":

	for linea in lineas:
		elementos = linea.split(',')
		operador = elementos[0]
		operando1 = int(elementos[1])
		operandos = elementos[2:]
		result = operando1

		if operador == "suma":
			for operando in operandos:
				result = calculadora.suma(result, int(operando))
		if operador == "resta":
			for operando in operandos:
				result = calculadora.resta(result, int(operando))
		if operador == "multiplica":
			for operando in operandos:
				result = calculadora.multiplicacion(result, int(operando))
		if operador == "divide":
			for operando in operandos:
				result = calculadora.division(result, int(operando))
			
		print(result)
