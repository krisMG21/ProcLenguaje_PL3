// Generated from c:/Users/socra/Documents/GitHub/ProcLenguaje_PL3/BasicMejorado.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BasicMejoradoParser}.
 */
public interface BasicMejoradoListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BasicMejoradoParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BasicMejoradoParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(BasicMejoradoParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(BasicMejoradoParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void enterLetStmt(BasicMejoradoParser.LetStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void exitLetStmt(BasicMejoradoParser.LetStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#opStmt}.
	 * @param ctx the parse tree
	 */
	void enterOpStmt(BasicMejoradoParser.OpStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#opStmt}.
	 * @param ctx the parse tree
	 */
	void exitOpStmt(BasicMejoradoParser.OpStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(BasicMejoradoParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(BasicMejoradoParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void enterInputStmt(BasicMejoradoParser.InputStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void exitInputStmt(BasicMejoradoParser.InputStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(BasicMejoradoParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(BasicMejoradoParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(BasicMejoradoParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(BasicMejoradoParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(BasicMejoradoParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(BasicMejoradoParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#repeatStmt}.
	 * @param ctx the parse tree
	 */
	void enterRepeatStmt(BasicMejoradoParser.RepeatStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#repeatStmt}.
	 * @param ctx the parse tree
	 */
	void exitRepeatStmt(BasicMejoradoParser.RepeatStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void enterKeyStmt(BasicMejoradoParser.KeyStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void exitKeyStmt(BasicMejoradoParser.KeyStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(BasicMejoradoParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(BasicMejoradoParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOp(BasicMejoradoParser.LogicalOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOp(BasicMejoradoParser.LogicalOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOp(BasicMejoradoParser.ComparisonOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOp(BasicMejoradoParser.ComparisonOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(BasicMejoradoParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(BasicMejoradoParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(BasicMejoradoParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(BasicMejoradoParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BasicMejoradoParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(BasicMejoradoParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link BasicMejoradoParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(BasicMejoradoParser.FunctionCallContext ctx);
}