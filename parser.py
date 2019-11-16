# -*- enconding: utf-8 -*-
#!/usr/bin/python
import ply.yacc as yacc
import os
from lexer import *
import sys

VERBOSE = 1


def p_cuerpo_fun(p):
    'cuerpo_fun : lista_sentencias '
    pass


def p_cuerpo_estructura(p):
    'cuerpo_estructura : DELIMITADOR1 lista_sentencias DELIMITADOR2'
    pass


def p_lista_sentencias(p):
    '''lista_sentencias : lista_sentencias sentencias 
    |   empty'''
    pass



def p_sentencias(p):
    '''sentencias : var_declaration
    |   fun_declaraciones 
    |   empty'''
    pass


def p_var_declaration(p):
    '''var_declaration : ENTERO ID
    |   LETRA ID
    |   ENTERO ID IGUAL NUMERO
    |   ENTERO ID IGUAL ID
    |   LETRA ID IGUAL ID 
    |   LETRA ID IGUAL CADENA
    |   empty '''
    pass

def p_fun_declaraciones(p):
    '''fun_declaraciones : fun_iteracion fun_declaraciones
    |   empty'''
    pass

def p_fun_iteracion(p):
    '''fun_iteracion : DE CORCHETE1 var IGUAL NUMERO SEPARADOR var IGUALIGUAL NUMERO CORCHETE2 cuerpo_estructura
    |   DURANTE CORCHETE1 expression CORCHETE2 cuerpo_estructura 
    |   SI CORCHETE1 expression CORCHETE2 cuerpo_estructura
    |   SI CORCHETE1 expression CORCHETE2 cuerpo_estructura SINO cuerpo_estructura
    |   SI CORCHETE1 expression CORCHETE2 cuerpo_estructura SINO SI CORCHETE1 expression CORCHETE2 cuerpo_estructura'''
    pass


def p_expression(p):
    '''expression : var operadores var
    | NUMERO operadores NUMERO
    | NUMERO operadores var
    | var operadores NUMERO '''
    pass



def p_operadores(p):
    '''operadores : MENOR 
    |   MENORQUE
    |   MAYOR
    |   MAYORQUE
    |   DIFERENTE
    |   IGUALIGUAL'''
    pass



def sintax(t):
    os.system("g++ -Wall "+t)
    pass


def p_var(p):
    'var : ID'
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" , str(p.lexer.lineno),"  Error de Contexto " , str(p.value))
        else:
            print ("Error en Lexico linea: " ,str(lexer.lexer.lineno))
            pass
    else:
        raise Exception('Syntax', 'error')

parser = yacc.yacc()



