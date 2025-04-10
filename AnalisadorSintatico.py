import ply.yacc as yacc
from AnalisadorLexico import *
from GramaticaAbstrata import *
import PrettyPrinter as pp

#ANALISADOR SINTÁTICO DE KOTLIN

def p_KotlinFile(p):
    """KotlinFile : ShebangLine packageHeader importList topLevelObject"""
    p[0] = KotlinFile(p[1], p[2], p[3], p[4])

def p_ShebangLine(p):
    """ShebangLine : HASH NOT ID"""
    p[0] = ShebangLine(p[3])

def p_packageHeader(p):
    """packageHeader : PACKAGE ID"""
    p[0] = PackageHeader(p[2])

def p_importList(p):
    """importList : importList importHeader"""
    p[0] = ImportList(p[2])

def p_importList2(p):
    """importList : importHeader"""
    p[0] = ImportList(p[1])
    
def p_importHeader(p):
    """importHeader : IMPORT ID"""
    p[0] = ImportHeader(p[2])
    
def p_topLevelObject(p):
    """topLevelObject : topLevelObject functionDeclaration"""
    p[0] = TopLevelObject(p[1], p[2])

def p_topLevelObject2(p):
    """topLevelObject : functionDeclaration"""
    p[0] = TopLevelObject(None, p[1])

def p_functionDeclaration(p):
    """functionDeclaration : FUN ID LPAREN params RPAREN block"""
    p[0] = FunctionDeclaration(p[2], p[4], None, p[6])

def p_functionDeclaration2(p):
    """functionDeclaration : FUN ID LPAREN params RPAREN COLON type block"""
    p[0] = FunctionDeclaration(p[2], p[4], p[7], p[8])

def p_functionDeclaration3(p):
    """functionDeclaration : FUN ID LPAREN RPAREN COLON type block"""
    p[0] = FunctionDeclaration(p[2], None, p[6], p[7])

def p_functionDeclaration4(p):
    """functionDeclaration : FUN ID LPAREN RPAREN block"""
    p[0] = FunctionDeclaration(p[2], None, None, p[5])

def p_params(p):
    """params : ID COLON type"""
    p[0] = Params(p[1], p[3], None)

def p_Params2(p):
    """params : ID COLON type COMMA params"""
    p[0] = Params(p[1], p[3], p[5])

def p_type(p):
    """type : TYPE_INT"""
    p[0] = TypeInt(p[1])

def p_type2(p):
    """type : TYPE_STRING"""
    p[0] = TypeString(p[1])

def p_type3(p):
    """type : TYPE_BOOLEAN"""
    p[0] = TypeBoolean(p[1])

def p_type4(p):
    """type : TYPE_FLOAT"""
    p[0] = TypeFloat(p[1])

def p_block(p):
    """block : LBRACE RBRACE"""
    
def p_block2(p):
    """block : LBRACE statements RBRACE"""
    p[0] = Block(p[2])

def p_statements(p):
    """statements : statements statement"""
    p[0] = StatementsComposto(p[1], p[2])

def p_statements2(p):
    """statements : statement"""
    p[0] = Statements(p[1])

def p_statement(p):
    """statement : expression"""
    p[0] = ExpressionStatement(p[1])

def p_statement2(p):
    """statement : variableDeclaration"""
    p[0] = VariableDeclarationStatement(p[1])

def p_statement3(p):
    """statement : variableAssignment"""
    p[0] = VariableAssigmentStatement(p[1])

def p_statement4(p):
    """statement : IF LPAREN expression RPAREN block elseStatement"""
    p[0] = IfStatement(p[3], p[5], p[6])

def p_statement5(p):
    """statement : IF LPAREN expression RPAREN block"""
    p[0] = IfStatement(p[3], p[5], None)

def p_elseStatement(p):
    """elseStatement : ELSE block"""
    p[0] = ElseStatement(p[2])

def p_statement7(p):
    """statement : forLoop"""
    p[0] = LoopStatementFor(p[1]) 

def p_statement8(p):
    """statement : whileLoop"""
    p[0] = LoopStatementWhile(p[1])

def p_statement9(p):
    """statement : returnStatement"""
    p[0] = ReturnStatement(p[1])

def p_expression(p):
    """expression : disjunction"""
    p[0] = Expression(p[1])
    
def p_disjunction(p):
    """disjunction : disjunction OR conjunction"""
    p[0] = Disjunction(p[1], p[2])

def p_disjunction2(p):
    """disjunction : conjunction"""
    p[0] = Disjunction(None, p[1])
    
def p_conjunction(p):
    """conjunction : conjunction AND equality"""
    p[0] = Conjunction(p[1], p[3])

def p_conjunction2(p):
    """conjunction : equality"""
    p[0] = Conjunction(None, p[1])
    
def p_equality(p):
    """equality : equality operadoresEquality comparation"""
    p[0] = Equality(p[1], p[2], p[3])

def p_equality2(p):
    """equality : comparation"""
    p[0] = Equality(None, None, p[1])

def p_operadoresEquality(p):
    """operadoresEquality : EQUAL"""
    p[0] = OperadoresEqualityIgual(p[1])

def p_operadoresEquality(p):
    """operadoresEquality : DIFFERENT"""
    p[0] = OperadoresEqualityDifferent(p[1])

def p_comparation(p):
    """comparation : comparation operadoresComparation inExpression"""
    p[0] = Comparation(p[1], p[2], p[3])

def p_comparation2(p):
    """comparation : inExpression"""
    p[0] = Comparation(None, None, p[1])

def p_operadoresComparation(p):
    """operadoresComparation : LESS"""
    p[0] = OperadoresComparationLess(p[1])
    
def p_operadoresComparation2(p):
    """operadoresComparation : GREATER"""
    p[0] = OperadoresComparationGreater(p[1])

def p_operadoresComparation3(p):
    """operadoresComparation : LESSEQ"""
    p[0] = OperadoresComparationLessEq(p[1])

def p_operadoresComparation4(p):
    """operadoresComparation : GREATEREQ"""
    p[0] = OperadoresComparationGreaterEq(p[1])
    
def p_inExpression(p):
    """inExpression : inExpression IN additive"""
    p[0] = InExpression(p[1], p[3])

def p_inExpression2(p):
    """inExpression : additive"""
    p[0] = InExpression(None, p[1])

def p_additive(p):
    """additive : additive aditivos multiplicative"""
    p[0] = Additive(p[1], p[2], p[3])

def p_additive2(p):
    """additive : multiplicative"""
    p[0] = Additive(None, None, p[1])

def p_aditivos(p):
    """aditivos : PLUS"""
    p[0] = AditivosPlus(p[1])

def p_aditivos2(p):
    """aditivos : MINUS"""
    p[0] = AditivosMinus(p[1])
    
def p_multiplicative(p):
    """multiplicative : multiplicative multiplicadores resto"""
    p[0] = Multiplicative(p[1], p[2], p[3])

def p_multiplicative2(p):
    """multiplicative : resto"""
    p[0] = Multiplicative(None, None, p[1])

def p_multiplicadores(p):
    """multiplicadores : TIMES"""
    p[0] = MultiplicadoresTimes(p[1])

def p_multiplicadores2(p):
    """multiplicadores : DIVIDE"""
    p[0] = MultiplicadoresDivide(p[1])

def p_resto(p):
    """resto : ID"""
    p[0] = RestoID(p[1])

def p_resto2(p):
    """resto : STRING"""
    p[0] = RestoString(p[1])

def p_resto3(p):
    """resto : NUMBER"""
    p[0] = RestoNumber(p[1])

def p_resto4(p):
    """resto : BOOLEAN"""
    p[0] = RestoBoolean(p[1])

def p_resto5(p):
    """resto : functionDeclaration"""
    p[0] = RestoFunctionDeclaration(p[1])

def p_resto6(p):
    """resto : functionCall"""
    p[0] = RestoFunctionCall(p[1])


def p_variableDeclaration(p):
    """variableDeclaration : VAR ID COLON type ASSIGN expression"""
    p[0] = VariableDeclaration(p[2], p[4], p[6])

def p_variableDeclaration2(p):
    """variableDeclaration : VAR ID COLON type"""
    p[0] = VariableDeclaration(p[2], p[4], None)


def p_variableAssignment(p):
    """variableAssignment : ID ASSIGN expression"""
    p[0] = VariableAssignmentAssign(p[1], p[2], p[3])

def p_variableAssignment2(p):
    """variableAssignment : ID PLUSEQ expression"""
    p[0] = VariableAssignmentPlusEq(p[1], p[2], p[3])

def p_variableAssignment3(p):
    """variableAssignment : ID MINUSEQ expression"""
    p[0] = VariableAssignmentMinusEq(p[1], p[2], p[3])

def p_variableAssignment4(p):
    """variableAssignment : ID TIMESEQ expression"""
    p[0] = VariableAssignmentTimesEq(p[1], p[2], p[3])

def p_variableAssignment5(p):
    """variableAssignment : ID DIVIDEEQ expression"""
    p[0] = VariableAssignmentDivideEq(p[1], p[2], p[3])

def p_forLoop(p):
    """forLoop : FOR LPAREN expression RPAREN block"""
    p[0] = ForLoop(p[3], p[5])

def p_whileLoop(p):
    """whileLoop : WHILE LPAREN expression RPAREN block"""
    p[0] = WhileLoop(p[3], p[5])
    

def p_returnStatement(p):
    """returnStatement : RETURN expression"""
    p[0] = ReturnStatement(p[2])


def p_functionCall(p):
    """functionCall : ID LPAREN listaParametros RPAREN"""
    p[0] = FunctionCall(p[1], p[3])

def p_functionCall2(p):
    """functionCall : ID LPAREN RPAREN"""
    p[0] = FunctionCall(p[1], None)

def p_listaParametros(p):
    """listaParametros : expression COMMA listaParametros"""
    p[0] = ListaParametros(p[1], p[3])

def p_listaParametros2(p):
    """listaParametros : expression"""
    p[0] = ListaParametros(p[1], None)

def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

lexer = lex.lex()
parser = yacc.yacc()
result = parser.parse("""

""")

visitor = pp.PrettyPrinter()
result.accept(visitor)

#Exemplo 1
'''#! kotlin

package exemplo

import kotlin

fun main() {
    var num: Int = 10

    if (num > 5) {
        println("O número é maior que 5")
    } else {
        println("O número é menor ou igual a 5")
    }
}'''

#Exemplo 2
'''#! kotlin

package exemplo

import kotlin

fun main() {
    for (i in 5) {
        println(i)
    }
}'''

#Exemplo 3
'''#! kotlin

package exemplo

import kotlin

fun main() {
    var x: Int = 1
    while (x <= 5) {
        println(x)
        x = x + 1
    }
}'''

#Exemplo 4
'''#! kotlin

package exemplo

import kotlin

fun soma(a: Int, b: Int): Int {
    return a + b + 1
}

fun main() {
    var x: Int = 10
    var y: Int = 5
    var resultado: Int = 0
    resultado = soma(x, y)
}'''










'''data = """
#! kotlin

package exemplo

import kotlin

fun soma(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    var x: Int = 10
    var y: Int = 5
    var resultado: Int = 0
    resultado = soma(x, y)
}
"""

lexer.input(data)'''