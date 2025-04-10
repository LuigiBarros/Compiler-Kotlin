class PrettyPrinter():
    def VisitKotlinFile(self, kotlinfile):
        kotlinfile.shebangline.accept(self)
        kotlinfile.packageheader.accept(self)
        kotlinfile.importlist.accept(self)
        kotlinfile.toplevelobject.accept(self)

    def VisitShebangLine(self, shebangline):
        print("#! ",end="")
        print(shebangline.id)

    def VisitPackageHeader(self, packageheader):
        print("package ",end="")
        print(packageheader.id)

    def VisitImportList(self, importlist):
        importlist.importheader.accept(self)

    def VisitImportHeader(self, importheader):
        print("import ",end="")
        print(importheader.id)

    def VisitTopLevelObject(self, multitoplevelobject):
        if multitoplevelobject.toplevelobject is not None:
            multitoplevelobject.toplevelobject.accept(self)
        multitoplevelobject.functiondeclaration.accept(self)

    def VisitFunctionDeclaration(self, functiondeclaration):
        print("fun ", end="")
        print(functiondeclaration.id, end="")
        print("(", end="")
        if functiondeclaration.params is not None:
            functiondeclaration.params.accept(self)
        print(") ", end="")
        if functiondeclaration.type is not None:
            print(": ", end="")
            functiondeclaration.type.accept(self)
        functiondeclaration.block.accept(self)

    def VisitParams(self, params):
        print(params.id, end="")
        print(": ", end="")
        if params.type is not None:
            params.type.accept(self)
        if params.params is not None:
            print(", ", end="")
            params.params.accept(self)

    def VisitTypeInt(self, typeint):
        print(typeint.int,end="")

    def VisitTypeString(self, typestring):
        print(typestring.string,end="")

    def VisitTypeBoolean(self, typeboolean):
        print(typeboolean.boolean,end="")

    def VisitTypeFloat(self, typefloat):
        print(typefloat.float,end="")

    def VisitBlock(self, block):
        print("{")
        if hasattr(block, 'statements') and block.statements is not None:
            block.statements.accept(self)
        print("}")

    def VisitStatementsComposto(self, statements):
        if statements is not None:
            statements.statements.accept(self)
            statements.statement.accept(self)

    def VisitStatements(self, statements):
        statements.statement.accept(self)

    def VisitExpressionStatement(self, expressionstatement):
        expressionstatement.expression.accept(self)

    def VisitVariableDeclarationStatement(self, variabledeclarationstatement):
        variabledeclarationstatement.variabledeclaration.accept(self)
    
    def VisitVariableAssigmentStatement(self, variableassigmentstatement):
        variableassigmentstatement.variableassigment.accept(self)

    def VisitReturnStatement(self, returnstatement):
        returnstatement.returnstatement.accept(self)

    def VisitExpression(self, expression):
        expression.disjunction.accept(self)

    def VisitDisjunction(self, disjunction):
        if disjunction.disjunction is not None:
            disjunction.disjunction.accept(self)
            print("||", end="")
        disjunction.conjunction.accept(self)

    def VisitConjunction(self, conjunction):
        if conjunction.conjunction is not None:
            conjunction.conjunction.accept(self)
            print("&&", end="")
        conjunction.equality.accept(self)

    def VisitEquality(self, equality):
        if equality.equality is not None:
            equality.equality.accept(self)
            equality.operadoresequality.accept(self)
        equality.comparation.accept(self)

    def VisitOperadoresEqualityIgual(self, equalityigual):
        print("==",end="")

    def VisitOperadoresDifferent(self, equalitydifferent):
        print("!=",end="")

    def VisitComparation(self, comparation):
        if comparation.comparation is not None:
            comparation.comparation.accept(self)
            comparation.operadorescomparation.accept(self)
        comparation.inexpression.accept(self)

    def VisitComparationLess(self, comparationless):
        print(" < ",end="")
    
    def VisitComparationGreater(self, comparationgreater):
        print(" > ",end="")

    def VisitComparationLessEq(self, comparationlesseq):
        print(" <= ",end="")

    def VisitComparationGreaterEq(self, comparationgreatereq):
        print(" >= ",end="")
    
    def VisitInExpression(self, inexpression):
        if inexpression.inexpression is not None:
            inexpression.inexpression.accept(self)
            print(" in ",end="")
        inexpression.additive.accept(self)

    def VisitAdditive(self, additive):
        if additive.additive is not None:
            additive.additive.accept(self)
            additive.aditivos.accept(self)
        additive.multiplicative.accept(self)

    def VisitAditivosPlus(self, aditivosplus):
        print(" + ",end="")

    def VisitAditivosMinus(self, aditivosminus):
        print(" - ",end="")

    def VisitMultiplicative(self, multiplicative):
        if multiplicative.multiplicative is not None:
            multiplicative.multiplicative.accept(self)
        if multiplicative.multiplicadores is not None:
            multiplicative.multiplicadores.accept(self)
        multiplicative.resto.accept(self)
    
    def VisitMultiplicadoresTimes(self, multiplicadorestimes):
        print(" * ",end="")

    def VisitMultiplicadoresDivide(self, multiplicadoresdivide):
        print(" / ",end="")

    def VisitRestoID(self, restoid):
        print(restoid.id,end="")

    def VisitRestoString(self, restostring):
        print(restostring.string,end="")

    def VisitRestoNumber(self, restonumber):
        print(restonumber.number,end="")

    def VisitRestoBoolean(self, restoboolean):
        print(restoboolean.boolean,end="")

    def VisitRestoFunctionDeclaration(self, functiondeclaration):
        functiondeclaration.functiondeclaration.accept(self)

    def VisitRestoFunctionCall(self, restofunctioncall):
        restofunctioncall.functioncall.accept(self)

    def VisitVariableDeclaration(self, variabledeclaration):
        print("var ",end="")
        print(variabledeclaration.id,end="")
        print(": ",end="")
        variabledeclaration.type.accept(self)
        print(" = ",end="")
        variabledeclaration.expression.accept(self)
        print("")

    def VisitVariableAssigmentAssign(self, variableassigmentassign):
        print(variableassigmentassign.id,end="")
        print(" = ",end="")
        variableassigmentassign.expression.accept(self)
        print("")

    def VisitVariableAssignmentPlusEq(self, variableassignmentpluseq):
        print(variableassignmentpluseq.id,end="")
        print(" += ",end="")
        variableassignmentpluseq.expression.accept(self)
        print("")

    def VisitVariableAssignmentMinusEq(self, variableassignmentminuseq):
        print(variableassignmentminuseq.id,end="")
        print(" -= ",end="")
        variableassignmentminuseq.expression.accept(self)
        print("")

    def VisitVariableAssignmentTimesEq(self, variableassignmenttimeseq):
        print(variableassignmenttimeseq.id,end="")
        print(" *= ",end="")
        variableassignmenttimeseq.expression.accept(self)
        print("")

    def VisitVariableAssignmentDivideEq(self, variableassignmentdivideeq):
        print(variableassignmentdivideeq.id,end="")
        print(" /= ",end="")
        variableassignmentdivideeq.expression.accept(self)
        print("")

    def VisitIfStatement(self, ifstatement):
        print("if (",end="")
        ifstatement.expression.accept(self)
        print(") ",end="")
        ifstatement.block.accept(self)
        if ifstatement.elsestatement is not None:
            ifstatement.elsestatement.accept(self)

    def VisitElseStatement(self, elsestatement):
        print("else",end="")
        elsestatement.block.accept(self)

    def VisitLoopStatementFor(self, loopstatementfor):
        loopstatementfor.forloop.accept(self)

    def VisitLoopStatementWhile(self, loopstatementwhile):
        loopstatementwhile.whileloop.accept(self)

    def VisitForLoop(self, forloop):
        print("for (",end="")
        forloop.expression.accept(self)
        print(") ",end="")
        forloop.block.accept(self)

    def VisitWhileLoop(self, whileloop):
        print("while (",end="")
        whileloop.expression.accept(self)
        print(") ",end="")
        whileloop.block.accept(self)

    def VisitReturnStatement(self, returnstatement):
        print("return ",end="")
        returnstatement.expression.accept(self)

    def VisitFunctionCall(self, functioncall):
        print(functioncall.functioncall.id, end="")
        print("(", end="")
        if functioncall.functioncall.listaparametros is not None:
            functioncall.functioncall.listaparametros.accept(self)
        print(")",end="")

    def VisitListaParametros(self, listaparametros):
        listaparametros.expression.accept(self)
        if listaparametros.listaparametros is not None:
            print(", ", end="")
            listaparametros.listaparametros.accept(self)
