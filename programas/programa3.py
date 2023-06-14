# -*- coding: utf-8 -*-

import sys
import io
import nltk

# SV: Secuencia de variables
# func: Función
# VAR: variable
# EB: Expreción Booleana
# AB: Expresión booleana atómica (?
# EA: Expresión aritmética
# A: Expresión aritmética atómica
# K: Constante
# X: Variable
# S: Slice
# IF: Invocación de Funciones
# LC: Linea de código
# BC: Bloque de código
# ITE: If-Then-Else
# VLC: Varias Lineas de Código

# grammar definition
grammar = """
defFunc -> 'def' func'('SV')'':' BC
BC -> LC | VLC | ITE | '{' BC '}' | ITR | BC BC
ITE -> 'if' EB':' BC | 'if' EB':' BC 'else'':' BC
ITR -> 'for' A 'in' 'range''('EA','EA')'':' BC | 'while' EB':' BC | 'for' A 'in' 'range''('EA')'':' BC
VLC -> LC LC | LC VLC
LC -> ASSIGN';'
ASSIGN -> ToAssign '=' ToAssign | ToAssign '=' func | ToAssign '=' EB | ToAssign '=' EA | 'return' EB | 'return' EA
ToAssign -> VAR | SLICING
SLICING -> VAR'['EA']' | VAR'['EA':'']' | VAR'['':'EA']' | VAR'['EA':'EA']' | VAR'['EA':'EA':'EA']'
SV -> VAR | VAR','SV
IF -> func'('EA')' | func'('VAR')'
func -> 'f1' | 'f2' | 'f3' | 'f4' | 'f5' | 'f6' | 'f7' | 'f8' | 'f9' | 'f10' | 'len' | 'range'

EB -> AB | 'not' EB | EB 'and' EB | EB 'or' EB | VAR | K | '('EB')'
AB -> EA '==' EA | EA '!''=' EA | EA '>''=' EA | EA '<''=' EA | EA '<' EA | EA '>' EA | 'True' | 'False'

EA -> A | '('EA')' | EA '+' EA | EA '*''*' EA | EA '//' EA | EA '-' EA | EA '%' EA | EA '*' EA | EA '/' EA
A ->  K | VAR | unidad | IF | SLICING
unidad -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
K -> 'k1' | 'k2' | 'k3' | 'k4' | 'k5' | 'k6' | 'k7' | 'k8' | 'k9' | 'k10'
VAR -> 'x1' | 'x2' | 'x3' | 'x4' | 'x5' | 'x6' | 'x7' | 'x8' | 'x9' | 'x10' | 'x' | 'i' | 'j' | 'k' | 'arr' | 'n' | 'left' | 'right' | 'mid'
"""


def parse(s, grammar):
        
    # parser
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)
    
    # tokenize
    s_tokenized = nltk.word_tokenize(s)

    # parse
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s, grammar)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE VOCABULARIO"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
