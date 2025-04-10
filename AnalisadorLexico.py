import ply.lex as lex

# ANALISADOR LÉXICO EM KOTLIN

# Palavras reservadas
reserved = {
    'import': 'IMPORT',
    'package': 'PACKAGE',
    'fun': 'FUN',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL',
    'Int': 'TYPE_INT',
    'String': 'TYPE_STRING',
    'Boolean': 'TYPE_BOOLEAN',
    'Float': 'TYPE_FLOAT',
}

# Todos os tokens, incluindo palavras reservadas
tokens = [
    'ID',
    'NUMBER',
    'STRING',
    'FLOAT',
    'BOOLEAN',
    
    # Operadores
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',

    # Atribuição 
    'ASSIGN', 'PLUSEQ', 'MINUSEQ', 'TIMESEQ', 'DIVIDEEQ',

    # Comparação 
    'EQUAL', 'DIFFERENT', 'LESS', 'GREATER', 'LESSEQ', 'GREATEREQ',

    # Lógico
    'AND', 'OR', 'NOT',

    # Delimitadores
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'COLON', 'DOUBLEQUOTES',

    # Demais tokens
    'HASH',
] + list(reserved.values())

# Regras de expressões regulares com tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\*\*'

t_ASSIGN = r'='
t_PLUSEQ = r'\+='
t_MINUSEQ = r'-='
t_TIMESEQ = r'\*='
t_DIVIDEEQ = r'/='

t_EQUAL = r'=='
t_DIFFERENT = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESSEQ = r'<='
t_GREATEREQ = r'>='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{' 
t_RBRACE = r'}'
t_COMMA = r','
t_COLON = r':'
t_DOUBLEQUOTES = r'"'
t_HASH = r'\#'
t_BOOLEAN = r'true|false'

# Caracteres ignorados (espaços e tabs)
t_ignore = ' \t'

# Regras de expressões regulares com ações 
def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT_SINGLE(t):
    r'//.*'
    pass

def t_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir lexer
lexer = lex.lex()

def main():
    f = open("input.kt", "r")
    lexer = lex.lex(debug=1)
    lexer.input(f.read())
    print('\n\n# Lexer output:')
    for tok in lexer:
        print(f'type: {tok.type}, value: {tok.value}')

if __name__ == "__main__":
    main()
