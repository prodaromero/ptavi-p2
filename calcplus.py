#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija

fichero = open('Operaciones', 'r')

lineas = fichero.readlines()

primera_linea = lineas[0]

calculadora = calcoohija.Calcoohija()

for linea in lineas:
	elems = linea.split(',')

	if elems[0] == "suma":
		result = int(elems[1])
		for result in elems[:-1]:
			result = calculadora.suma(result, int(elems[:-1]))

	print(result)
