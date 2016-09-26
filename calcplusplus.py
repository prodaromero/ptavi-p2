#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoo
import calcoohija


if __name__ == "__main__":

    calculadora = calcoohija.Calcoohija()

    argumento = sys.argv[1]

    try:
        fichero = open(argumento, 'r')
    except:
        sys.exit("Error: file not found")

    with open(argumento) as operaciones:
        lineas = csv.reader(operaciones)

        for linea in lineas:
            operador = linea[0]
            operando1 = int(linea[1])
            operandos = linea[2:]
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
