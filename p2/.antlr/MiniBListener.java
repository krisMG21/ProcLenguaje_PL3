// Generated from c:/Users/socra/Documents/GitHub/ProcLenguaje_PL3/p2/MiniB.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiniBParser}.
 */
public interface MiniBListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiniBParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MiniBParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniBParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MiniBParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniBParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MiniBParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniBParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MiniBParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Let}
	 * labeled alternative in {@link MiniBParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void enterLet(MiniBParser.LetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Let}
	 * labeled alternative in {@link MiniBParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void exitLet(MiniBParser.LetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Op}
	 * labeled alternative in {@link MiniBParser#opStmt}.
	 * @param ctx the parse tree
	 */
	void enterOp(MiniBParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Op}
	 * labeled alternative in {@link MiniBParser#opStmt}.
	 * @param ctx the parse tree
	 */
	void exitOp(MiniBParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Print}
	 * labeled alternative in {@link MiniBParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint(MiniBParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Print}
	 * labeled alternative in {@link MiniBParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint(MiniBParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Input}
	 * labeled alternative in {@link MiniBParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void enterInput(MiniBParser.InputContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Input}
	 * labeled alternative in {@link MiniBParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void exitInput(MiniBParser.InputContext ctx);
	/**
	 * Enter a parse tree produced by the {@code If}
	 * labeled alternative in {@link MiniBParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIf(MiniBParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code If}
	 * labeled alternative in {@link MiniBParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIf(MiniBParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code For}
	 * labeled alternative in {@link MiniBParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterFor(MiniBParser.ForContext ctx);
	/**
	 * Exit a parse tree produced by the {@code For}
	 * labeled alternative in {@link MiniBParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitFor(MiniBParser.ForContext ctx);
	/**
	 * Enter a parse tree produced by the {@code While}
	 * labeled alternative in {@link MiniBParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile(MiniBParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code While}
	 * labeled alternative in {@link MiniBParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile(MiniBParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Repeat}
	 * labeled alternative in {@link MiniBParser#repeatStmt}.
	 * @param ctx the parse tree
	 */
	void enterRepeat(MiniBParser.RepeatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Repeat}
	 * labeled alternative in {@link MiniBParser#repeatStmt}.
	 * @param ctx the parse tree
	 */
	void exitRepeat(MiniBParser.RepeatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Continue}
	 * labeled alternative in {@link MiniBParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinue(MiniBParser.ContinueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Continue}
	 * labeled alternative in {@link MiniBParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinue(MiniBParser.ContinueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Exit}
	 * labeled alternative in {@link MiniBParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void enterExit(MiniBParser.ExitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Exit}
	 * labeled alternative in {@link MiniBParser#keyStmt}.
	 * @param ctx the parse tree
	 */
	void exitExit(MiniBParser.ExitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniBParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOp(MiniBParser.LogicalOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniBParser#logicalOp}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOp(MiniBParser.LogicalOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniBParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOp(MiniBParser.ComparisonOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniBParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOp(MiniBParser.ComparisonOpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PlusOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void enterPlusOperation(MiniBParser.PlusOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PlusOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void exitPlusOperation(MiniBParser.PlusOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MinusOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void enterMinusOperation(MiniBParser.MinusOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MinusOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void exitMinusOperation(MiniBParser.MinusOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void enterMulOperation(MiniBParser.MulOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void exitMulOperation(MiniBParser.MulOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DivOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void enterDivOperation(MiniBParser.DivOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DivOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void exitDivOperation(MiniBParser.DivOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ModOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void enterModOperation(MiniBParser.ModOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ModOperation}
	 * labeled alternative in {@link MiniBParser#arithmeticOp}.
	 * @param ctx the parse tree
	 */
	void exitModOperation(MiniBParser.ModOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Not}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterNot(MiniBParser.NotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Not}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitNot(MiniBParser.NotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code condExp}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondExp(MiniBParser.CondExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code condExp}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondExp(MiniBParser.CondExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterComparison(MiniBParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitComparison(MiniBParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Logical}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterLogical(MiniBParser.LogicalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Logical}
	 * labeled alternative in {@link MiniBParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitLogical(MiniBParser.LogicalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StringExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterStringExpression(MiniBParser.StringExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StringExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitStringExpression(MiniBParser.StringExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIdExpression(MiniBParser.IdExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIdExpression(MiniBParser.IdExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParenExpression(MiniBParser.ParenExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParenExpression(MiniBParser.ParenExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NumberExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNumberExpression(MiniBParser.NumberExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NumberExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNumberExpression(MiniBParser.NumberExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArithmeticExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(MiniBParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArithmeticExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(MiniBParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionCallExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExpression(MiniBParser.FunctionCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionCallExpression}
	 * labeled alternative in {@link MiniBParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExpression(MiniBParser.FunctionCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ValFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterValFunction(MiniBParser.ValFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ValFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitValFunction(MiniBParser.ValFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LenFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterLenFunction(MiniBParser.LenFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LenFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitLenFunction(MiniBParser.LenFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IsNanFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterIsNanFunction(MiniBParser.IsNanFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IsNanFunction}
	 * labeled alternative in {@link MiniBParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitIsNanFunction(MiniBParser.IsNanFunctionContext ctx);
}