import ply.lex as lex

tokens = [
    "L_LLAVE",         
    "R_LLAVE",         
    "L_CORCHETE",      
    "R_CORCHETE",      
    "COMA",            
    "DOS_PUNTOS",      
    "BOOLEAN",         
    "NULL",            
    "NUMBER",          
    "STRING",          
    "ATTRIBUTE"        
]

t_L_LLAVE = r'\{'
t_R_LLAVE = r'\}'
t_L_CORCHETE = r'\['
t_R_CORCHETE = r'\]'
t_COMA = r','
t_DOS_PUNTOS = r':'

def t_BOOLEAN(t):
    r'\s*(true|false)'
    t.value = True if t.value == "true" else False
    return t

def t_NULL(t):
    r'\s*null'
    t.value = None
    return t

def t_NUMBER(t):
    r'\s*-?\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_STRING(t):
    r'\s*"([^"]*)"'
    t.value = t.value[1:-1]
    return t

def t_ATTRIBUTE(t):
    r'\s*"(\w)":\s*'
    t.value = t.value[1:].split(':')[0].strip('"') 
    return t

t_ignore = " \t\n\r"

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
