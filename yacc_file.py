from ply import yacc
from lexer_file import tokens

def p_json(p):
    '''json : object
            | array'''
    p[0] = p[1]

def p_object(p):
    '''object : L_LLAVE key_value_list R_LLAVE
              | L_LLAVE R_LLAVE'''
    if len(p) == 4:
        p[0] = dict(p[2])
    else:
        p[0] = {}

def p_key_value_list(p):
    '''key_value_list : key_value
                      | key_value COMA key_value_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_key_value(p):
    '''key_value : ATTRIBUTE value
                | STRING DOS_PUNTOS value'''
    if len(p) == 3:  
        p[0] = (p[1], p[2])
    else:  
        p[0] = (p[1], p[3])

def p_array(p):
    '''array : L_CORCHETE value_list R_CORCHETE
             | L_CORCHETE R_CORCHETE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_value_list(p):
    '''value_list : value
                  | value COMA value_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value(p):
    '''value : object
             | array
             | STRING
             | NUMBER
             | BOOLEAN
             | NULL'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en token '{p.type}', valor '{p.value}' en línea {p.lineno}")
    else:
        print("Error de sintaxis en EOF")

parser = yacc.yacc()