if __name__ is not None and "." in __name__:
    from gen.pyGramParser import pyGramParser
else:
    from gen.pyGramParser import pyGramParser
from gen.pyGramListener import pyGramListener
from SematicErrors import *

class myListener(pyGramListener):
    symbol_table = {}
    functions_args = {}
    stack_block = []

    def __isNumeric(self, type):
        return (type == 'float') or (type == 'int')

    def enterL_type(self, ctx:pyGramParser.L_typeContext):
        self.stack_block.append('function')
        ctx_type = ctx.TYPE(0).getText() if ctx.TYPE(0).getText() != 'int' else 'integer'
        function_id = ctx.ID(0).getText()
        self.symbol_table[function_id] = ctx_type

        args = []
        for arg_id,arg_type in list(zip(ctx.ID()[1:], ctx.TYPE()[1:])):
            arg_type_text = arg_type.getText() if arg_type.getText() != 'int' else 'integer'
            self.symbol_table[arg_id.getText()] = arg_type_text
            args.append(arg_type_text)

        self.functions_args[function_id] = args

    def enterL_void(self, ctx:pyGramParser.L_voidContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        self.symbol_table[function_id] = 'NoneType'

        args = []
        for arg_id,arg_type in list(zip(ctx.ID()[1:], ctx.TYPE())):
            arg_type_text = arg_type.getText() if arg_type.getText() != 'int' else 'integer'
            self.symbol_table[arg_id.getText()] = arg_type_text
            args.append(arg_type_text)

        self.functions_args[function_id] = args

    def enterFunction_call(self, ctx:pyGramParser.Function_callContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table.keys():
            raise UndeclaredVariable(ctx_id)

    def enterR_for(self, ctx:pyGramParser.R_forContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table.keys():
            raise UndeclaredVariable(ctx_id)

        if self.symbol_table[ctx_id] != 'integer':
            raise UnexpectedTypeError('integer', self.symbol_table[ctx_id])

        self.stack_block.append('loop')

    def enterR_while(self, ctx:pyGramParser.R_whileContext):
        self.stack_block.append('loop')

    def enterR_return(self, ctx: pyGramParser.R_returnContext):
        if 'function' not in self.stack_block:
            raise ReturnException()

    def enterR_break(self, ctx:pyGramParser.R_breakContext):
        if 'loop' not in self.stack_block:
            raise BreakException()

    def exitR_for(self, ctx:pyGramParser.R_forContext):
        self.stack_block.pop()

    def exitR_while(self, ctx:pyGramParser.R_whileContext):
        self.stack_block.pop()

    def exitDeclaration(self, ctx:pyGramParser.DeclarationContext):
        ctx_type = ctx.TYPE().getText() if ctx.TYPE().getText() != 'int' else 'integer'

        for token in ctx.ID():
            self.symbol_table[token.getText()] = ctx_type

        print(self.symbol_table)

    def exitL_type(self, ctx:pyGramParser.L_typeContext):
        self.stack_block.pop()

        for arg_id in ctx.ID()[1:]:
            del self.symbol_table[arg_id]

    def exitL_void(self, ctx:pyGramParser.L_voidContext):
        self.stack_block.pop()

        for arg_id in ctx.ID()[1:]:
            del self.symbol_table[arg_id]

    def exitFunction_call(self, ctx:pyGramParser.Function_callContext):
        function_id = ctx.ID().getText()

        if len(self.functions_args[function_id]) != len(ctx.expr()):
            raise MissingArgument(len(self.functions_args[function_id]), len(ctx.expr()))

        for expected, recieved in list(zip(self.functions_args[function_id], ctx.expr())):
            if expected != recieved.type:
                raise UnexpectedTypeError(expected, recieved.type)

        ctx.type = self.symbol_table[ctx.ID().getText()]

    def exitAssigment(self, ctx:pyGramParser.AssigmentContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table.keys():
            raise UndeclaredVariable(ctx_id)

        expected = self.symbol_table[ctx_id]
        recieved = ctx.expr().type
        if expected != recieved:
            raise UnexpectedTypeError(expected, recieved)

    def exitL_expr(self, ctx:pyGramParser.L_exprContext):
        ctx.type = ctx.expr().type

    def exitL_id(self, ctx:pyGramParser.L_idContext):
        teste = ctx.ID()
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table.keys():
            raise UndeclaredVariable(ctx_id)

        ctx.type = self.symbol_table[ctx_id]

    def exitL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        ctx.type = 'integer'

    def exitL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        ctx.type = 'float'

    def exitL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        ctx.type = 'string'

    def exitL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        ctx.type = 'boolean'

    def exitL_input(self, ctx:pyGramParser.L_inputContext):
        ctx.type = 'string'

    def exitL_function_call(self, ctx:pyGramParser.L_function_callContext):
        ctx.type = ctx.function_call().type

    def exitOr_logic(self, ctx: pyGramParser.Or_logicContext):
        if (ctx.children[0].type != 'boolean' or ctx.children[2].type != 'boolean'):
            raise ExprTypeError(ctx.children[0].type, ctx.children[2].type, ctx.children[1].symbol.text)
            return
        ctx.type = 'boolean'

    def exitAnd_logic(self, ctx: pyGramParser.Or_logicContext):
        if (ctx.children[0].type != 'boolean' or ctx.children[2].type != 'boolean'):
            raise ExprTypeError(ctx.children[0].type, ctx.children[2].type, ctx.children[1].symbol.text)
            return
        ctx.type = 'boolean'

    def exitComp_logic(self, ctx: pyGramParser.Comp_logicContext):
        ctx.type = 'boolean'

    def exitEq_logic(self, ctx: pyGramParser.Eq_logicContext):
        ctx.type = 'boolean'

    def exitSum_minus(self, ctx: pyGramParser.Sum_minusContext):
        if self.__isNumeric(ctx.children[0].type) and self.__isNumeric(ctx.children[2].type):
            if ctx.children[0].type == 'float' or ctx.children[2].type == 'float':
                ctx.type = 'float'
            else:
                ctx.type = 'int'
            return
        raise ExprTypeError(ctx.children[0].type, ctx.children[2].type, ctx.children[1].symbol.text)

    def exitTime_div(self, ctx:pyGramParser.Time_divContext):
        if self.__isNumeric(ctx.children[0].type) and self.__isNumeric(ctx.children[2].type):
            if ctx.children[0].type == 'float' or ctx.children[2].type == 'float':
                ctx.type = 'float'
            else:
                ctx.type = 'int'
            return
        raise ExprTypeError(ctx.children[0].type, ctx.children[2].type, ctx.children[1].symbol.text)

    def exitMinus_not(self, ctx:pyGramParser.Minus_notContext):
        if ctx.children[0].symbol.text == '-': #minus
            if (self.__isNumeric(ctx.children[1].type)):
                ctx.type = ctx.children[1].type
                return
            raise ExprTypeError(ctx.children[1].type, ctx.children[0].symbol.text)
        elif ctx.children[0].symbol.text == 'not': #not
            if (ctx.children[1].type == 'boolean'):
                ctx.type = 'boolean'
                return
            raise ExprTypeError(ctx.children[1].type, ctx.children[0].symbol.text)

    def exitE_term(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term().type

    def exitE_term2(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term2().type

    def exitE_term3(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term3().type

    def exitE_term4(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term4().type

    def exitE_term5(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term5().type

    def exitE_term6(self, ctx: pyGramParser.E_termContext):
        ctx.type = ctx.term6().type

    def exitE_factor(self, ctx:pyGramParser.E_factorContext):
        ctx.type = ctx.factor().type