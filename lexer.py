# -*- encondig: utf-8 -*-
import ply.lex as lex
import os

reservadas = ['DE','SI','ENTERO','LETRA','SINO','DURANTE']

tokens = reservadas+['MAS','MENOS','POR','ENTRE','MENOR','MENORQUE','MAYOR','MAYORQUE',
                    'IGUAL','IGUALIGUAL','DIFERENTE','CORCHETE1','CORCHETE2',
                    'DELIMITADOR1','DELIMITADOR2','COMILLAS','SEPARADOR','CADENA','ID','NUMERO']


t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_ENTRE = r'\/'
t_IGUAL = r'\='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_CORCHETE1 = r'\['
t_CORCHETE2 = r'\]'
t_DELIMITADOR1 = r'\{'
t_DELIMITADOR2 = r'\}'
t_SEPARADOR = r'\->'
t_COMILLAS = r'\"'




def t_SINO(t):
    r'sino'
    return t


def t_SI(t):
    r'si'
    return t


def t_ENTERO(t):
    r'num'
    return t


def t_LETRA(t):
    r'str'
    return t


def t_DURANTE(t):
    r'durante'
    return t


def t_DE(t):
    r'de'
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t



def t_CADENA(t):
    r'\"[a-z0-9_]+\"'
    return t


def t_MENORQUE(t):
    r'<='
    return t


def t_MAYORQUE(t):
    r'>='
    return t


def t_IGUALIGUAL(t):
    r'=='
    return t



def t_DIFERENTE(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'



def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)



def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

def Analizador_lexico():
    a = input("direccion: ")
    if ( os.path.exists (a)):
        f = open(a)
        data = f.read()
        f.close()
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")

