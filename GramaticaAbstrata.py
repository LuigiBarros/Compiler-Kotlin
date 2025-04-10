class AbstractKotlinFile():
    def accept(visitor):
        pass

class KotlinFile(AbstractKotlinFile):
    def __init__(self, shebangline, packageheader, importlist, toplevelobject):
        self.shebangline = shebangline
        self.packageheader = packageheader
        self.importlist = importlist
        self.toplevelobject = toplevelobject

    def accept(self, visitor):
        visitor.VisitKotlinFile(self)

class AbstractShebangLine():
    def accept(visitor):
        pass

class ShebangLine(AbstractShebangLine):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.VisitShebangLine(self)
    
class AbstractPackageHeader():
    def accept(visitor):
        pass

class PackageHeader(AbstractPackageHeader):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.VisitPackageHeader(self)

class AbstractImportList():
    def accept(visitor):
        pass

class ImportList(AbstractImportList):
    def __init__(self, importheader):
        self.importheader = importheader

    def accept(self, visitor):
        visitor.VisitImportList(self)

class AbstractImportHeader():
    def accept(visitor):
        pass

class ImportHeader(AbstractImportHeader):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.VisitImportHeader(self)

class AbstractTopLevelObject():
    def accept(visitor):
        pass

class TopLevelObject(AbstractTopLevelObject):
    def __init__(self, toplevelobject, functiondeclaration):
        self.toplevelobject = toplevelobject
        self.functiondeclaration = functiondeclaration

    def accept(self, visitor):
        visitor.VisitTopLevelObject(self)

class AbstractFunctionDeclaration:
    def accept(visitor):
        pass

class FunctionDeclaration(AbstractFunctionDeclaration):
    def __init__(self, id, params, type, block):
        self.id = id
        self.params = params
        self.type = type
        self.block = block

    def accept(self, visitor):
        visitor.VisitFunctionDeclaration(self)

class AbstractParams():
     def accept(visitor):
        pass
     
class Params(AbstractParams):
    def __init__(self, id, type, params):
        self.id = id
        self.type = type
        self.params = params

    def accept(self, visitor):
        visitor.VisitParams(self)
        
class AbstractType():
    def accept(visitor):
        pass

class TypeInt(AbstractType):
    def __init__(self, int):
        self.int = int

    def accept(self, visitor):
        visitor.VisitTypeInt(self)

class TypeString(AbstractType):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        visitor.VisitTypeString(self)

class TypeBoolean(AbstractType):
    def __init__(self, boolean):
        self.boolean = boolean

    def accept(self, visitor):
        visitor.VisitTypeBoolean(self)

class TypeFloat(AbstractType):
    def __init__(self, float):
        self.float = float

    def accept(self, visitor):
        visitor.VisitTypeFloat(self)

class AbstractBlock():
    def accept(visitor):
        pass

class Block(AbstractBlock):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.VisitBlock(self)

class AbstractStatemens():
    def accept(visitor):
        pass

class StatementsComposto(AbstractStatemens):
    def __init__(self, statements, statement):
        self.statements = statements
        self.statement = statement

    def accept(self, visitor):
        visitor.VisitStatementsComposto(self)

class Statements(AbstractStatemens):
    def __init__(self, statement):
        self.statement = statement

    def accept(self, visitor):
        visitor.VisitStatements(self)

class AbstractStatement():
    def accept(visitor):
        pass

class ExpressionStatement(AbstractStatement):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitExpressionStatement(self)

class VariableDeclarationStatement(AbstractStatement):
    def __init__(self, variabledeclaration):
        self.variabledeclaration = variabledeclaration

    def accept(self, visitor):
        visitor.VisitVariableDeclarationStatement(self)

class VariableAssigmentStatement(AbstractStatement):
    def __init__(self, variableassigment):
        self.variableassigment = variableassigment

    def accept(self, visitor):
        visitor.VisitVariableAssigmentStatement(self)

class IfStatement(AbstractStatement):
    def __init__(self, expression, block, elsestatement):
        self.expression = expression
        self.block = block
        self.elsestatement = elsestatement

    def accept(self, visitor):
        visitor.VisitIfStatement(self)

class AbstractElseStatement():
    def accept(visitor):
        pass

class ElseStatement(AbstractElseStatement):
    def __init__(self, block):
        self.block = block

    def accept(self, visitor):
        visitor.VisitElseStatement(self)

class ReturnStatement(AbstractStatement):
    def __init__(self, returnstatement):
        self.returnstatement = returnstatement

    def accept(self, visitor):
        visitor.VisitReturnStatement(self)

class AbstractExpression():
    def accept(visitor):
        pass

class Expression(AbstractExpression):
    def __init__(self, disjunction):
        self.disjunction = disjunction

    def accept(self, visitor):
        visitor.VisitExpression(self)

class AbstractDisjunction():
    def accept(visitor):
        pass

class Disjunction(AbstractDisjunction):
    def __init__(self, disjunction, conjunction):
        self.disjunction = disjunction
        self.conjunction = conjunction

    def accept(self, visitor):
        visitor.VisitDisjunction(self)

class AbstractConjunction():
    def accept(visitor):
        pass

class Conjunction(AbstractConjunction):
    def __init__(self, conjunction, equality):
        self.conjunction = conjunction
        self.equality = equality

    def accept(self, visitor):
        visitor.VisitConjunction(self)

class AbstractEquality():
    def accept(visitor):
        pass

class Equality(AbstractEquality):
    def __init__(self, equality, operadoresequality, comparation):
        self.equality = equality
        self.operadoresequality = operadoresequality
        self.comparation = comparation

    def accept(self, visitor):
        visitor.VisitEquality(self)

class AbstractOperadoresEquality():
    def accept(visitor):
        pass

class OperadoresEqualityIgual(AbstractOperadoresEquality):
    def __init__(self, igual):
        self.igual = igual

    def accept(self, visitor):
        visitor.VisitOperadoresEqualityIgual(self)

class OperadoresEqualityDifferent(AbstractOperadoresEquality):
    def __init__(self, different):
        self.different = different

    def accept(self, visitor):
        visitor.VisitOperadoresDifferent(self)

class AbstractComparation():
    def accept(visitor):
        pass

class Comparation(AbstractComparation):
    def __init__(self, comparation, operadorescomparation, inexpression):
        self.comparation = comparation
        self.operadorescomparation = operadorescomparation
        self.inexpression = inexpression

    def accept(self, visitor):
        visitor.VisitComparation(self)

class AbstractOperadoresComparation():
    def accept(visitor):
        pass

class OperadoresComparationLess(AbstractOperadoresComparation):
    def __init__(self, less):
        self.less = less

    def accept(self, visitor):
        visitor.VisitComparationLess(self)

class OperadoresComparationGreater(AbstractOperadoresComparation):
    def __init__(self, greater):
        self.greater = greater

    def accept(self, visitor):
        visitor.VisitComparationGreater(self)

class OperadoresComparationLessEq(AbstractOperadoresComparation):
    def __init__(self, lesseq):
        self.lesseq = lesseq

    def accept(self, visitor):
        visitor.VisitComparationLessEq(self)

class OperadoresComparationGreaterEq(AbstractOperadoresComparation):
    def __init__(self, greatereq):
        self.greatereq = greatereq

    def accept(self, visitor):
        visitor.VisitComparationGreaterEq(self)

class AbstractInExpression():
    def accept(visitor):
        pass

class InExpression(AbstractInExpression):
    def __init__(self, inexpression, additive):
        self.inexpression = inexpression
        self.additive = additive

    def accept(self, visitor):
        visitor.VisitInExpression(self)

class AbstractAdditive():
    def accept(visitor):
        pass

class Additive(AbstractAdditive):
    def __init__(self, additive, aditivos, multiplicative):
        self.additive = additive
        self.aditivos = aditivos
        self.multiplicative = multiplicative

    def accept(self, visitor):
        visitor.VisitAdditive(self)

class AbstractAditivos():
    def accept(visitor):
        pass

class AditivosPlus(AbstractAditivos):
    def __init__(self, plus):
        self.plus = plus

    def accept(self, visitor):
        visitor.VisitAditivosPlus(self)

class AditivosMinus(AbstractAditivos):
    def __init__(self, minus):
        self.minus = minus

    def accept(self, visitor):
        visitor.VisitAditivosMinus(self)

class AbstractMultiplicative():
    def accept(visitor):
        pass

class Multiplicative(AbstractMultiplicative):
    def __init__(self, multiplicative, multiplicadores, resto):
        self.multiplicative = multiplicative
        self.multiplicadores = multiplicadores
        self.resto = resto

    def accept(self, visitor):
        visitor.VisitMultiplicative(self)

class AbstractMultiplicadores():
    def accept(visitor):
        pass

class MultiplicadoresTimes(AbstractMultiplicadores):
    def __init__(self, times):
        self.times = times

    def accept(self, visitor):
        visitor.VisitMultiplicadoresTimes(self)

class MultiplicadoresDivide(AbstractMultiplicadores):
    def __init__(self, divide):
        self.divide = divide

    def accept(self, visitor):
        visitor.VisitMultiplicadoresDivide(self)

class AbstractResto():
    def accept(visitor):
        pass

class RestoID(AbstractResto):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.VisitRestoID(self)

class RestoString(AbstractResto):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        visitor.VisitRestoString(self)

class RestoNumber(AbstractResto):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        visitor.VisitRestoNumber(self)

class RestoBoolean(AbstractResto):
    def __init__(self, boolean):
        self.boolean = boolean

    def accept(self, visitor):
        visitor.VistiRestoBoolean(self)

class RestoFunctionDeclaration(AbstractResto):
    def __init__(self, functiondeclaration):
        self.functiondeclaration = functiondeclaration

    def accept(self, visitor):
        visitor.VisitRestoFunctionDeclaration(self)

class RestoFunctionCall(AbstractResto):
    def __init__(self, functioncall):
        self.functioncall = functioncall
        
    def accept(self, visitor):
        visitor.VisitFunctionCall(self)

class AbstractVariableDeclaration():
    def accept(visitor):
        pass

class VariableDeclaration(AbstractVariableDeclaration):
    def __init__(self, id, type, expression):
        self.id = id
        self.type = type
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableDeclaration(self)

class AbstractVariableAssignment():
    def accept(visitor):
        pass

class VariableAssignmentAssign(AbstractVariableAssignment):
    def __init__(self, id, assign, expression):
        self.id = id
        self.assign = assign
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableAssigmentAssign(self)

class VariableAssignmentPlusEq(AbstractVariableAssignment):
    def __init__(self, id, pluseq, expression):
        self.id = id
        self.pluseq = pluseq
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableAssignmentPlusEq(self)

class VariableAssignmentMinusEq(AbstractVariableAssignment):
    def __init__(self, id, minuseq, expression):
        self.id = id
        self.minuseq = minuseq
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableAssignmentMinusEq(self)

class VariableAssignmentTimesEq(AbstractVariableAssignment):
    def __init__(self, id, timeseq, expression):
        self.id = id
        self.timeseq = timeseq
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableAssignmentTimesEq(self)

class VariableAssignmentDivideEq(AbstractVariableAssignment):
    def __init__(self, id, divideeq, expression):
        self.id = id
        self.divideeq = divideeq
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitVariableAssignmentDivideEq(self)

    def accept(self, visitor):
        visitor.VisitIfStatement(self)

class AbstractLoopStatement():
    def accept(visitor):
        pass

class LoopStatementFor(AbstractLoopStatement):
    def __init__(self, forloop):
        self.forloop = forloop

    def accept(self, visitor):
        visitor.VisitLoopStatementFor(self)

class LoopStatementWhile(AbstractLoopStatement):
    def __init__(self, whileloop):
        self.whileloop = whileloop

    def accept(self, visitor):
        visitor.VisitLoopStatementWhile(self)

class AbstractForLoop():
    def accept(visitor):
        pass

class ForLoop(AbstractForLoop):
    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    def accept(self, visitor):
        visitor.VisitForLoop(self)

class AbstractWhileLoop():
    def accept(visitor):
        pass

class WhileLoop(AbstractWhileLoop):
    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    def accept(self, visitor):
        visitor.VisitWhileLoop(self)

class AbstractReturnStatement():
    def accept(visitor):
        pass

class ReturnStatement(AbstractReturnStatement):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.VisitReturnStatement(self)

class AbstractFunctionCall():
    def accept(visitor):
        pass

class FunctionCall(AbstractFunctionCall):
    def __init__(self, id, listaparametros):
        self.id = id
        self.listaparametros = listaparametros

    def accept(self, visitor):
        visitor.VisitRestoFunctionCall(self)  # Em vez de VisitFunctionCall

class AbstractListaParametros():
    def accept(visitor):
        pass

class ListaParametros(AbstractListaParametros):
    def __init__(self, expression, listaparametros):
        self.expression = expression
        self.listaparametros = listaparametros

    def accept(self, visitor):
        visitor.VisitListaParametros(self)