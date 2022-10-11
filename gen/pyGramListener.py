# Generated from /home/jpedro/workspace/jpedrodsp/novo_compilador/pyGram.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pyGramParser import pyGramParser
else:
    from pyGramParser import pyGramParser

# This class defines a complete listener for a parse tree produced by pyGramParser.
class pyGramListener(ParseTreeListener):

    # Enter a parse tree produced by pyGramParser#program.
    def enterProgram(self, ctx:pyGramParser.ProgramContext):
        pass

    # Exit a parse tree produced by pyGramParser#program.
    def exitProgram(self, ctx:pyGramParser.ProgramContext):
        pass


    # Enter a parse tree produced by pyGramParser#global_variables_declaration.
    def enterGlobal_variables_declaration(self, ctx:pyGramParser.Global_variables_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#global_variables_declaration.
    def exitGlobal_variables_declaration(self, ctx:pyGramParser.Global_variables_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#functions_declaration.
    def enterFunctions_declaration(self, ctx:pyGramParser.Functions_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#functions_declaration.
    def exitFunctions_declaration(self, ctx:pyGramParser.Functions_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#main.
    def enterMain(self, ctx:pyGramParser.MainContext):
        pass

    # Exit a parse tree produced by pyGramParser#main.
    def exitMain(self, ctx:pyGramParser.MainContext):
        pass


    # Enter a parse tree produced by pyGramParser#function_body_statements.
    def enterFunction_body_statements(self, ctx:pyGramParser.Function_body_statementsContext):
        pass

    # Exit a parse tree produced by pyGramParser#function_body_statements.
    def exitFunction_body_statements(self, ctx:pyGramParser.Function_body_statementsContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_type.
    def enterL_type(self, ctx:pyGramParser.L_typeContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_type.
    def exitL_type(self, ctx:pyGramParser.L_typeContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_void.
    def enterL_void(self, ctx:pyGramParser.L_voidContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_void.
    def exitL_void(self, ctx:pyGramParser.L_voidContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_return.
    def enterR_return(self, ctx:pyGramParser.R_returnContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_return.
    def exitR_return(self, ctx:pyGramParser.R_returnContext):
        pass


    # Enter a parse tree produced by pyGramParser#function_call.
    def enterFunction_call(self, ctx:pyGramParser.Function_callContext):
        pass

    # Exit a parse tree produced by pyGramParser#function_call.
    def exitFunction_call(self, ctx:pyGramParser.Function_callContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_for.
    def enterR_for(self, ctx:pyGramParser.R_forContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_for.
    def exitR_for(self, ctx:pyGramParser.R_forContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_while.
    def enterR_while(self, ctx:pyGramParser.R_whileContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_while.
    def exitR_while(self, ctx:pyGramParser.R_whileContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_break.
    def enterR_break(self, ctx:pyGramParser.R_breakContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_break.
    def exitR_break(self, ctx:pyGramParser.R_breakContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_if.
    def enterR_if(self, ctx:pyGramParser.R_ifContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_if.
    def exitR_if(self, ctx:pyGramParser.R_ifContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_else.
    def enterR_else(self, ctx:pyGramParser.R_elseContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_else.
    def exitR_else(self, ctx:pyGramParser.R_elseContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_print.
    def enterR_print(self, ctx:pyGramParser.R_printContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_print.
    def exitR_print(self, ctx:pyGramParser.R_printContext):
        pass


    # Enter a parse tree produced by pyGramParser#variable_declaration.
    def enterVariable_declaration(self, ctx:pyGramParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#variable_declaration.
    def exitVariable_declaration(self, ctx:pyGramParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#single_variable_declaration.
    def enterSingle_variable_declaration(self, ctx:pyGramParser.Single_variable_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#single_variable_declaration.
    def exitSingle_variable_declaration(self, ctx:pyGramParser.Single_variable_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#multiple_variable_declaration.
    def enterMultiple_variable_declaration(self, ctx:pyGramParser.Multiple_variable_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#multiple_variable_declaration.
    def exitMultiple_variable_declaration(self, ctx:pyGramParser.Multiple_variable_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_assigment.
    def enterE_assigment(self, ctx:pyGramParser.E_assigmentContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_assigment.
    def exitE_assigment(self, ctx:pyGramParser.E_assigmentContext):
        pass


    # Enter a parse tree produced by pyGramParser#input.
    def enterInput(self, ctx:pyGramParser.InputContext):
        pass

    # Exit a parse tree produced by pyGramParser#input.
    def exitInput(self, ctx:pyGramParser.InputContext):
        pass


    # Enter a parse tree produced by pyGramParser#or_logic.
    def enterOr_logic(self, ctx:pyGramParser.Or_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#or_logic.
    def exitOr_logic(self, ctx:pyGramParser.Or_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term.
    def enterE_term(self, ctx:pyGramParser.E_termContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_term.
    def exitE_term(self, ctx:pyGramParser.E_termContext):
        pass


    # Enter a parse tree produced by pyGramParser#and_logic.
    def enterAnd_logic(self, ctx:pyGramParser.And_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#and_logic.
    def exitAnd_logic(self, ctx:pyGramParser.And_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term2.
    def enterE_term2(self, ctx:pyGramParser.E_term2Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term2.
    def exitE_term2(self, ctx:pyGramParser.E_term2Context):
        pass


    # Enter a parse tree produced by pyGramParser#comp_logic.
    def enterComp_logic(self, ctx:pyGramParser.Comp_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#comp_logic.
    def exitComp_logic(self, ctx:pyGramParser.Comp_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term3.
    def enterE_term3(self, ctx:pyGramParser.E_term3Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term3.
    def exitE_term3(self, ctx:pyGramParser.E_term3Context):
        pass


    # Enter a parse tree produced by pyGramParser#eq_logic.
    def enterEq_logic(self, ctx:pyGramParser.Eq_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#eq_logic.
    def exitEq_logic(self, ctx:pyGramParser.Eq_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term4.
    def enterE_term4(self, ctx:pyGramParser.E_term4Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term4.
    def exitE_term4(self, ctx:pyGramParser.E_term4Context):
        pass


    # Enter a parse tree produced by pyGramParser#sum_minus.
    def enterSum_minus(self, ctx:pyGramParser.Sum_minusContext):
        pass

    # Exit a parse tree produced by pyGramParser#sum_minus.
    def exitSum_minus(self, ctx:pyGramParser.Sum_minusContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term5.
    def enterE_term5(self, ctx:pyGramParser.E_term5Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term5.
    def exitE_term5(self, ctx:pyGramParser.E_term5Context):
        pass


    # Enter a parse tree produced by pyGramParser#e_term6.
    def enterE_term6(self, ctx:pyGramParser.E_term6Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term6.
    def exitE_term6(self, ctx:pyGramParser.E_term6Context):
        pass


    # Enter a parse tree produced by pyGramParser#time_div.
    def enterTime_div(self, ctx:pyGramParser.Time_divContext):
        pass

    # Exit a parse tree produced by pyGramParser#time_div.
    def exitTime_div(self, ctx:pyGramParser.Time_divContext):
        pass


    # Enter a parse tree produced by pyGramParser#minus_not.
    def enterMinus_not(self, ctx:pyGramParser.Minus_notContext):
        pass

    # Exit a parse tree produced by pyGramParser#minus_not.
    def exitMinus_not(self, ctx:pyGramParser.Minus_notContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_factor.
    def enterE_factor(self, ctx:pyGramParser.E_factorContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_factor.
    def exitE_factor(self, ctx:pyGramParser.E_factorContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_expr.
    def enterL_expr(self, ctx:pyGramParser.L_exprContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_expr.
    def exitL_expr(self, ctx:pyGramParser.L_exprContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_function_call.
    def enterL_function_call(self, ctx:pyGramParser.L_function_callContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_function_call.
    def exitL_function_call(self, ctx:pyGramParser.L_function_callContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_id.
    def enterL_id(self, ctx:pyGramParser.L_idContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_id.
    def exitL_id(self, ctx:pyGramParser.L_idContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_int_value.
    def enterL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_int_value.
    def exitL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_float_value.
    def enterL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_float_value.
    def exitL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_str_value.
    def enterL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_str_value.
    def exitL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_bool_value.
    def enterL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_bool_value.
    def exitL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_input.
    def enterR_input(self, ctx:pyGramParser.R_inputContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_input.
    def exitR_input(self, ctx:pyGramParser.R_inputContext):
        pass



del pyGramParser