// Generated from c:/Users/ruben/Desktop/Uni/4/Lenguaje/ProcLenguaje_PL3/p2/MiniB.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MiniBParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, NOT=5, AND=6, OR=7, LET=8, PRINT=9, INPUT=10, 
		IF=11, ELSE=12, FOR=13, TO=14, NEXT=15, WHILE=16, REPEAT=17, UNTIL=18, 
		CONTINUE=19, EXIT=20, END=21, THEN=22, MOD=23, VAL=24, LEN=25, ISNAN=26, 
		REM=27, DIM=28, REDIM=29, LT=30, GT=31, LE=32, GE=33, EQ=34, PLUS=35, 
		MINUS=36, MUL=37, DIV=38, ID=39, NUMBER=40, STRING_LITERAL=41, NEWLINE=42, 
		COMMENT=43, WS=44;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_letStmt = 2, RULE_opStmt = 3, 
		RULE_arrayOpStmt = 4, RULE_printStmt = 5, RULE_inputStmt = 6, RULE_ifStmt = 7, 
		RULE_forStmt = 8, RULE_whileStmt = 9, RULE_repeatStmt = 10, RULE_keyStmt = 11, 
		RULE_dimStmt = 12, RULE_redimStmt = 13, RULE_logicalOp = 14, RULE_comparisonOp = 15, 
		RULE_arithmeticOp = 16, RULE_condition = 17, RULE_expression = 18, RULE_functionCall = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "letStmt", "opStmt", "arrayOpStmt", "printStmt", 
			"inputStmt", "ifStmt", "forStmt", "whileStmt", "repeatStmt", "keyStmt", 
			"dimStmt", "redimStmt", "logicalOp", "comparisonOp", "arithmeticOp", 
			"condition", "expression", "functionCall"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'['", "']'", "'('", "')'", null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "'<'", "'>'", "'<='", "'>='", 
			"'='", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "NOT", "AND", "OR", "LET", "PRINT", "INPUT", 
			"IF", "ELSE", "FOR", "TO", "NEXT", "WHILE", "REPEAT", "UNTIL", "CONTINUE", 
			"EXIT", "END", "THEN", "MOD", "VAL", "LEN", "ISNAN", "REM", "DIM", "REDIM", 
			"LT", "GT", "LE", "GE", "EQ", "PLUS", "MINUS", "MUL", "DIV", "ID", "NUMBER", 
			"STRING_LITERAL", "NEWLINE", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MiniB.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniBParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MiniBParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(MiniBParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniBParser.NEWLINE, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(40);
					statement();
					setState(42); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(41);
						match(NEWLINE);
						}
						}
						setState(44); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==NEWLINE );
					}
					} 
				}
				setState(50);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
				{
				setState(51);
				statement();
				}
			}

			setState(54);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public LetStmtContext letStmt() {
			return getRuleContext(LetStmtContext.class,0);
		}
		public OpStmtContext opStmt() {
			return getRuleContext(OpStmtContext.class,0);
		}
		public ArrayOpStmtContext arrayOpStmt() {
			return getRuleContext(ArrayOpStmtContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public InputStmtContext inputStmt() {
			return getRuleContext(InputStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public RepeatStmtContext repeatStmt() {
			return getRuleContext(RepeatStmtContext.class,0);
		}
		public KeyStmtContext keyStmt() {
			return getRuleContext(KeyStmtContext.class,0);
		}
		public DimStmtContext dimStmt() {
			return getRuleContext(DimStmtContext.class,0);
		}
		public RedimStmtContext redimStmt() {
			return getRuleContext(RedimStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				letStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				opStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				arrayOpStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				printStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				inputStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(61);
				ifStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(62);
				forStmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(63);
				whileStmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(64);
				repeatStmt();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(65);
				keyStmt();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(66);
				dimStmt();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(67);
				redimStmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetStmtContext extends ParserRuleContext {
		public LetStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStmt; }
	 
		public LetStmtContext() { }
		public void copyFrom(LetStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetContext extends LetStmtContext {
		public ExpressionContext exp;
		public TerminalNode LET() { return getToken(MiniBParser.LET, 0); }
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public TerminalNode EQ() { return getToken(MiniBParser.EQ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetContext(LetStmtContext ctx) { copyFrom(ctx); }
	}

	public final LetStmtContext letStmt() throws RecognitionException {
		LetStmtContext _localctx = new LetStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_letStmt);
		try {
			_localctx = new LetContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(LET);
			setState(71);
			match(ID);
			setState(72);
			match(EQ);
			setState(73);
			((LetContext)_localctx).exp = expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpStmtContext extends ParserRuleContext {
		public OpStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opStmt; }
	 
		public OpStmtContext() { }
		public void copyFrom(OpStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpContext extends OpStmtContext {
		public ExpressionContext exp;
		public ConditionContext cond;
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public TerminalNode EQ() { return getToken(MiniBParser.EQ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public OpContext(OpStmtContext ctx) { copyFrom(ctx); }
	}

	public final OpStmtContext opStmt() throws RecognitionException {
		OpStmtContext _localctx = new OpStmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_opStmt);
		try {
			_localctx = new OpContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
			setState(76);
			match(EQ);
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(77);
				((OpContext)_localctx).exp = expression(0);
				}
				break;
			case 2:
				{
				setState(78);
				((OpContext)_localctx).cond = condition();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayOpStmtContext extends ParserRuleContext {
		public ArrayOpStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayOpStmt; }
	 
		public ArrayOpStmtContext() { }
		public void copyFrom(ArrayOpStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArrayOpContext extends ArrayOpStmtContext {
		public ExpressionContext exp;
		public ConditionContext cond;
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public TerminalNode EQ() { return getToken(MiniBParser.EQ, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public ArrayOpContext(ArrayOpStmtContext ctx) { copyFrom(ctx); }
	}

	public final ArrayOpStmtContext arrayOpStmt() throws RecognitionException {
		ArrayOpStmtContext _localctx = new ArrayOpStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_arrayOpStmt);
		try {
			_localctx = new ArrayOpContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(ID);
			setState(82);
			match(T__0);
			setState(83);
			((ArrayOpContext)_localctx).exp = expression(0);
			setState(84);
			match(T__1);
			setState(85);
			match(EQ);
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(86);
				((ArrayOpContext)_localctx).exp = expression(0);
				}
				break;
			case 2:
				{
				setState(87);
				((ArrayOpContext)_localctx).cond = condition();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
	 
		public PrintStmtContext() { }
		public void copyFrom(PrintStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends PrintStmtContext {
		public ExpressionContext exp;
		public TerminalNode PRINT() { return getToken(MiniBParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PrintContext(PrintStmtContext ctx) { copyFrom(ctx); }
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_printStmt);
		try {
			_localctx = new PrintContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(PRINT);
			setState(91);
			((PrintContext)_localctx).exp = expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputStmtContext extends ParserRuleContext {
		public InputStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputStmt; }
	 
		public InputStmtContext() { }
		public void copyFrom(InputStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InputContext extends InputStmtContext {
		public Token str;
		public TerminalNode INPUT() { return getToken(MiniBParser.INPUT, 0); }
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(MiniBParser.STRING_LITERAL, 0); }
		public InputContext(InputStmtContext ctx) { copyFrom(ctx); }
	}

	public final InputStmtContext inputStmt() throws RecognitionException {
		InputStmtContext _localctx = new InputStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_inputStmt);
		try {
			_localctx = new InputContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(INPUT);
			setState(94);
			((InputContext)_localctx).str = match(STRING_LITERAL);
			setState(95);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	 
		public IfStmtContext() { }
		public void copyFrom(IfStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends IfStmtContext {
		public ConditionContext cond;
		public StatementContext statif;
		public StatementContext statelse;
		public TerminalNode IF() { return getToken(MiniBParser.IF, 0); }
		public TerminalNode THEN() { return getToken(MiniBParser.THEN, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(MiniBParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniBParser.NEWLINE, i);
		}
		public TerminalNode END() { return getToken(MiniBParser.END, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(MiniBParser.ELSE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfContext(IfStmtContext ctx) { copyFrom(ctx); }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifStmt);
		int _la;
		try {
			_localctx = new IfContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(IF);
			setState(98);
			((IfContext)_localctx).cond = condition();
			setState(99);
			match(THEN);
			setState(100);
			match(NEWLINE);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
				{
				{
				setState(101);
				((IfContext)_localctx).statif = statement();
				setState(102);
				match(NEWLINE);
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(109);
				match(ELSE);
				setState(110);
				match(NEWLINE);
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
					{
					{
					setState(111);
					((IfContext)_localctx).statelse = statement();
					setState(112);
					match(NEWLINE);
					}
					}
					setState(118);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(121);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStmtContext extends ParserRuleContext {
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	 
		public ForStmtContext() { }
		public void copyFrom(ForStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ForContext extends ForStmtContext {
		public ExpressionContext exp1;
		public ExpressionContext exp2;
		public StatementContext stat;
		public TerminalNode FOR() { return getToken(MiniBParser.FOR, 0); }
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public TerminalNode EQ() { return getToken(MiniBParser.EQ, 0); }
		public TerminalNode TO() { return getToken(MiniBParser.TO, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(MiniBParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniBParser.NEWLINE, i);
		}
		public TerminalNode NEXT() { return getToken(MiniBParser.NEXT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ForContext(ForStmtContext ctx) { copyFrom(ctx); }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_forStmt);
		int _la;
		try {
			_localctx = new ForContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(FOR);
			setState(124);
			match(ID);
			setState(125);
			match(EQ);
			setState(126);
			((ForContext)_localctx).exp1 = expression(0);
			setState(127);
			match(TO);
			setState(128);
			((ForContext)_localctx).exp2 = expression(0);
			setState(129);
			match(NEWLINE);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
				{
				{
				setState(130);
				((ForContext)_localctx).stat = statement();
				setState(131);
				match(NEWLINE);
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			match(NEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	 
		public WhileStmtContext() { }
		public void copyFrom(WhileStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends WhileStmtContext {
		public ConditionContext cond;
		public StatementContext stat;
		public TerminalNode WHILE() { return getToken(MiniBParser.WHILE, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(MiniBParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniBParser.NEWLINE, i);
		}
		public TerminalNode END() { return getToken(MiniBParser.END, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhileContext(WhileStmtContext ctx) { copyFrom(ctx); }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whileStmt);
		int _la;
		try {
			_localctx = new WhileContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(WHILE);
			setState(141);
			((WhileContext)_localctx).cond = condition();
			setState(142);
			match(NEWLINE);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
				{
				{
				setState(143);
				((WhileContext)_localctx).stat = statement();
				setState(144);
				match(NEWLINE);
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeatStmtContext extends ParserRuleContext {
		public RepeatStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeatStmt; }
	 
		public RepeatStmtContext() { }
		public void copyFrom(RepeatStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepeatContext extends RepeatStmtContext {
		public StatementContext stat;
		public ConditionContext cond;
		public TerminalNode REPEAT() { return getToken(MiniBParser.REPEAT, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(MiniBParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniBParser.NEWLINE, i);
		}
		public TerminalNode UNTIL() { return getToken(MiniBParser.UNTIL, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public RepeatContext(RepeatStmtContext ctx) { copyFrom(ctx); }
	}

	public final RepeatStmtContext repeatStmt() throws RecognitionException {
		RepeatStmtContext _localctx = new RepeatStmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_repeatStmt);
		int _la;
		try {
			_localctx = new RepeatContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(REPEAT);
			setState(154);
			match(NEWLINE);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 550562901760L) != 0)) {
				{
				{
				setState(155);
				((RepeatContext)_localctx).stat = statement();
				setState(156);
				match(NEWLINE);
				}
				}
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(163);
			match(UNTIL);
			setState(164);
			((RepeatContext)_localctx).cond = condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyStmtContext extends ParserRuleContext {
		public KeyStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyStmt; }
	 
		public KeyStmtContext() { }
		public void copyFrom(KeyStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ContinueContext extends KeyStmtContext {
		public TerminalNode CONTINUE() { return getToken(MiniBParser.CONTINUE, 0); }
		public ContinueContext(KeyStmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExitContext extends KeyStmtContext {
		public TerminalNode EXIT() { return getToken(MiniBParser.EXIT, 0); }
		public ExitContext(KeyStmtContext ctx) { copyFrom(ctx); }
	}

	public final KeyStmtContext keyStmt() throws RecognitionException {
		KeyStmtContext _localctx = new KeyStmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_keyStmt);
		try {
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONTINUE:
				_localctx = new ContinueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				match(CONTINUE);
				}
				break;
			case EXIT:
				_localctx = new ExitContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				match(EXIT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DimStmtContext extends ParserRuleContext {
		public DimStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimStmt; }
	 
		public DimStmtContext() { }
		public void copyFrom(DimStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DimContext extends DimStmtContext {
		public ExpressionContext exp;
		public TerminalNode DIM() { return getToken(MiniBParser.DIM, 0); }
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DimContext(DimStmtContext ctx) { copyFrom(ctx); }
	}

	public final DimStmtContext dimStmt() throws RecognitionException {
		DimStmtContext _localctx = new DimStmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_dimStmt);
		try {
			_localctx = new DimContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(DIM);
			setState(171);
			match(ID);
			setState(172);
			match(T__0);
			setState(173);
			((DimContext)_localctx).exp = expression(0);
			setState(174);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RedimStmtContext extends ParserRuleContext {
		public RedimStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redimStmt; }
	 
		public RedimStmtContext() { }
		public void copyFrom(RedimStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RedimContext extends RedimStmtContext {
		public ExpressionContext exp;
		public TerminalNode REDIM() { return getToken(MiniBParser.REDIM, 0); }
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RedimContext(RedimStmtContext ctx) { copyFrom(ctx); }
	}

	public final RedimStmtContext redimStmt() throws RecognitionException {
		RedimStmtContext _localctx = new RedimStmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_redimStmt);
		try {
			_localctx = new RedimContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(REDIM);
			setState(177);
			match(ID);
			setState(178);
			match(T__0);
			setState(179);
			((RedimContext)_localctx).exp = expression(0);
			setState(180);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOpContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(MiniBParser.AND, 0); }
		public TerminalNode OR() { return getToken(MiniBParser.OR, 0); }
		public LogicalOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOp; }
	}

	public final LogicalOpContext logicalOp() throws RecognitionException {
		LogicalOpContext _localctx = new LogicalOpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_logicalOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonOpContext extends ParserRuleContext {
		public TerminalNode LT() { return getToken(MiniBParser.LT, 0); }
		public TerminalNode GT() { return getToken(MiniBParser.GT, 0); }
		public TerminalNode LE() { return getToken(MiniBParser.LE, 0); }
		public TerminalNode GE() { return getToken(MiniBParser.GE, 0); }
		public TerminalNode EQ() { return getToken(MiniBParser.EQ, 0); }
		public ComparisonOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonOp; }
	}

	public final ComparisonOpContext comparisonOp() throws RecognitionException {
		ComparisonOpContext _localctx = new ComparisonOpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_comparisonOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 33285996544L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArithmeticOpContext extends ParserRuleContext {
		public ArithmeticOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmeticOp; }
	 
		public ArithmeticOpContext() { }
		public void copyFrom(ArithmeticOpContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModOperationContext extends ArithmeticOpContext {
		public TerminalNode MOD() { return getToken(MiniBParser.MOD, 0); }
		public ModOperationContext(ArithmeticOpContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DivOperationContext extends ArithmeticOpContext {
		public TerminalNode DIV() { return getToken(MiniBParser.DIV, 0); }
		public DivOperationContext(ArithmeticOpContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PlusOperationContext extends ArithmeticOpContext {
		public TerminalNode PLUS() { return getToken(MiniBParser.PLUS, 0); }
		public PlusOperationContext(ArithmeticOpContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulOperationContext extends ArithmeticOpContext {
		public TerminalNode MUL() { return getToken(MiniBParser.MUL, 0); }
		public MulOperationContext(ArithmeticOpContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MinusOperationContext extends ArithmeticOpContext {
		public TerminalNode MINUS() { return getToken(MiniBParser.MINUS, 0); }
		public MinusOperationContext(ArithmeticOpContext ctx) { copyFrom(ctx); }
	}

	public final ArithmeticOpContext arithmeticOp() throws RecognitionException {
		ArithmeticOpContext _localctx = new ArithmeticOpContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_arithmeticOp);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
				_localctx = new PlusOperationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				match(PLUS);
				}
				break;
			case MINUS:
				_localctx = new MinusOperationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				match(MINUS);
				}
				break;
			case MUL:
				_localctx = new MulOperationContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(188);
				match(MUL);
				}
				break;
			case DIV:
				_localctx = new DivOperationContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(189);
				match(DIV);
				}
				break;
			case MOD:
				_localctx = new ModOperationContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(190);
				match(MOD);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	 
		public ConditionContext() { }
		public void copyFrom(ConditionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotContext extends ConditionContext {
		public ConditionContext cond;
		public TerminalNode NOT() { return getToken(MiniBParser.NOT, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public NotContext(ConditionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondExpContext extends ConditionContext {
		public ExpressionContext expr;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CondExpContext(ConditionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ConditionContext {
		public ExpressionContext left;
		public ComparisonOpContext op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ComparisonOpContext comparisonOp() {
			return getRuleContext(ComparisonOpContext.class,0);
		}
		public ComparisonContext(ConditionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalContext extends ConditionContext {
		public ExpressionContext left;
		public LogicalOpContext op;
		public ConditionContext right;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LogicalOpContext logicalOp() {
			return getRuleContext(LogicalOpContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public LogicalContext(ConditionContext ctx) { copyFrom(ctx); }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_condition);
		try {
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				_localctx = new ComparisonContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(193);
				((ComparisonContext)_localctx).left = expression(0);
				setState(194);
				((ComparisonContext)_localctx).op = comparisonOp();
				setState(195);
				((ComparisonContext)_localctx).right = expression(0);
				}
				break;
			case 2:
				_localctx = new NotContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(197);
				match(NOT);
				setState(198);
				((NotContext)_localctx).cond = condition();
				}
				break;
			case 3:
				_localctx = new LogicalContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(199);
				((LogicalContext)_localctx).left = expression(0);
				setState(200);
				((LogicalContext)_localctx).op = logicalOp();
				setState(201);
				((LogicalContext)_localctx).right = condition();
				}
				break;
			case 4:
				_localctx = new CondExpContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(203);
				((CondExpContext)_localctx).expr = expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringExpressionContext extends ExpressionContext {
		public TerminalNode STRING_LITERAL() { return getToken(MiniBParser.STRING_LITERAL, 0); }
		public StringExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdExpressionContext extends ExpressionContext {
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public IdExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenExpressionContext extends ExpressionContext {
		public ExpressionContext expr;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberExpressionContext extends ExpressionContext {
		public TerminalNode NUMBER() { return getToken(MiniBParser.NUMBER, 0); }
		public NumberExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArithmeticExpressionContext extends ExpressionContext {
		public ExpressionContext left;
		public ArithmeticOpContext op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArithmeticOpContext arithmeticOp() {
			return getRuleContext(ArithmeticOpContext.class,0);
		}
		public ArithmeticExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArrayAccessExpressionContext extends ExpressionContext {
		public ExpressionContext expr;
		public TerminalNode ID() { return getToken(MiniBParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArrayAccessExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallExpressionContext extends ExpressionContext {
		public FunctionCallContext fun;
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				_localctx = new ParenExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(207);
				match(T__2);
				setState(208);
				((ParenExpressionContext)_localctx).expr = expression(0);
				setState(209);
				match(T__3);
				}
				break;
			case 2:
				{
				_localctx = new FunctionCallExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(211);
				((FunctionCallExpressionContext)_localctx).fun = functionCall();
				}
				break;
			case 3:
				{
				_localctx = new NumberExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(212);
				match(NUMBER);
				}
				break;
			case 4:
				{
				_localctx = new StringExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(213);
				match(STRING_LITERAL);
				}
				break;
			case 5:
				{
				_localctx = new IdExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(214);
				match(ID);
				}
				break;
			case 6:
				{
				_localctx = new ArrayAccessExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(215);
				match(ID);
				setState(216);
				match(T__0);
				setState(217);
				((ArrayAccessExpressionContext)_localctx).expr = expression(0);
				setState(218);
				match(T__1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(228);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ArithmeticExpressionContext(new ExpressionContext(_parentctx, _parentState));
					((ArithmeticExpressionContext)_localctx).left = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(222);
					if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
					setState(223);
					((ArithmeticExpressionContext)_localctx).op = arithmeticOp();
					setState(224);
					((ArithmeticExpressionContext)_localctx).right = expression(8);
					}
					} 
				}
				setState(230);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	 
		public FunctionCallContext() { }
		public void copyFrom(FunctionCallContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IsNanFunctionContext extends FunctionCallContext {
		public ExpressionContext expr;
		public TerminalNode ISNAN() { return getToken(MiniBParser.ISNAN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IsNanFunctionContext(FunctionCallContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValFunctionContext extends FunctionCallContext {
		public ExpressionContext expr;
		public TerminalNode VAL() { return getToken(MiniBParser.VAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ValFunctionContext(FunctionCallContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LenFunctionContext extends FunctionCallContext {
		public ExpressionContext expr;
		public TerminalNode LEN() { return getToken(MiniBParser.LEN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LenFunctionContext(FunctionCallContext ctx) { copyFrom(ctx); }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_functionCall);
		try {
			setState(246);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAL:
				_localctx = new ValFunctionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				match(VAL);
				setState(232);
				match(T__2);
				setState(233);
				((ValFunctionContext)_localctx).expr = expression(0);
				setState(234);
				match(T__3);
				}
				break;
			case LEN:
				_localctx = new LenFunctionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				match(LEN);
				setState(237);
				match(T__2);
				setState(238);
				((LenFunctionContext)_localctx).expr = expression(0);
				setState(239);
				match(T__3);
				}
				break;
			case ISNAN:
				_localctx = new IsNanFunctionContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(241);
				match(ISNAN);
				setState(242);
				match(T__2);
				setState(243);
				((IsNanFunctionContext)_localctx).expr = expression(0);
				setState(244);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001,\u00f9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0004\u0000+\b\u0000"+
		"\u000b\u0000\f\u0000,\u0005\u0000/\b\u0000\n\u0000\f\u00002\t\u0000\u0001"+
		"\u0000\u0003\u00005\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001E\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003P\b\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004Y\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007i\b"+
		"\u0007\n\u0007\f\u0007l\t\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007s\b\u0007\n\u0007\f\u0007v\t\u0007\u0003"+
		"\u0007x\b\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u0086\b\b\n"+
		"\b\f\b\u0089\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0005\t\u0093\b\t\n\t\f\t\u0096\t\t\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u009f\b\n\n\n\f\n\u00a2\t\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0003\u000b\u00a9\b\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00c0"+
		"\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u00cd\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00dd\b\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00e3\b\u0012\n"+
		"\u0012\f\u0012\u00e6\t\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003"+
		"\u0013\u00f7\b\u0013\u0001\u0013\u0000\u0001$\u0014\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&\u0000\u0002\u0001\u0000\u0006\u0007\u0001\u0000\u001e\"\u010a\u0000"+
		"0\u0001\u0000\u0000\u0000\u0002D\u0001\u0000\u0000\u0000\u0004F\u0001"+
		"\u0000\u0000\u0000\u0006K\u0001\u0000\u0000\u0000\bQ\u0001\u0000\u0000"+
		"\u0000\nZ\u0001\u0000\u0000\u0000\f]\u0001\u0000\u0000\u0000\u000ea\u0001"+
		"\u0000\u0000\u0000\u0010{\u0001\u0000\u0000\u0000\u0012\u008c\u0001\u0000"+
		"\u0000\u0000\u0014\u0099\u0001\u0000\u0000\u0000\u0016\u00a8\u0001\u0000"+
		"\u0000\u0000\u0018\u00aa\u0001\u0000\u0000\u0000\u001a\u00b0\u0001\u0000"+
		"\u0000\u0000\u001c\u00b6\u0001\u0000\u0000\u0000\u001e\u00b8\u0001\u0000"+
		"\u0000\u0000 \u00bf\u0001\u0000\u0000\u0000\"\u00cc\u0001\u0000\u0000"+
		"\u0000$\u00dc\u0001\u0000\u0000\u0000&\u00f6\u0001\u0000\u0000\u0000("+
		"*\u0003\u0002\u0001\u0000)+\u0005*\u0000\u0000*)\u0001\u0000\u0000\u0000"+
		"+,\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000"+
		"\u0000-/\u0001\u0000\u0000\u0000.(\u0001\u0000\u0000\u0000/2\u0001\u0000"+
		"\u0000\u00000.\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u000014\u0001"+
		"\u0000\u0000\u000020\u0001\u0000\u0000\u000035\u0003\u0002\u0001\u0000"+
		"43\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u000056\u0001\u0000\u0000"+
		"\u000067\u0005\u0000\u0000\u00017\u0001\u0001\u0000\u0000\u00008E\u0003"+
		"\u0004\u0002\u00009E\u0003\u0006\u0003\u0000:E\u0003\b\u0004\u0000;E\u0003"+
		"\n\u0005\u0000<E\u0003\f\u0006\u0000=E\u0003\u000e\u0007\u0000>E\u0003"+
		"\u0010\b\u0000?E\u0003\u0012\t\u0000@E\u0003\u0014\n\u0000AE\u0003\u0016"+
		"\u000b\u0000BE\u0003\u0018\f\u0000CE\u0003\u001a\r\u0000D8\u0001\u0000"+
		"\u0000\u0000D9\u0001\u0000\u0000\u0000D:\u0001\u0000\u0000\u0000D;\u0001"+
		"\u0000\u0000\u0000D<\u0001\u0000\u0000\u0000D=\u0001\u0000\u0000\u0000"+
		"D>\u0001\u0000\u0000\u0000D?\u0001\u0000\u0000\u0000D@\u0001\u0000\u0000"+
		"\u0000DA\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000DC\u0001\u0000"+
		"\u0000\u0000E\u0003\u0001\u0000\u0000\u0000FG\u0005\b\u0000\u0000GH\u0005"+
		"\'\u0000\u0000HI\u0005\"\u0000\u0000IJ\u0003$\u0012\u0000J\u0005\u0001"+
		"\u0000\u0000\u0000KL\u0005\'\u0000\u0000LO\u0005\"\u0000\u0000MP\u0003"+
		"$\u0012\u0000NP\u0003\"\u0011\u0000OM\u0001\u0000\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000P\u0007\u0001\u0000\u0000\u0000QR\u0005\'\u0000\u0000"+
		"RS\u0005\u0001\u0000\u0000ST\u0003$\u0012\u0000TU\u0005\u0002\u0000\u0000"+
		"UX\u0005\"\u0000\u0000VY\u0003$\u0012\u0000WY\u0003\"\u0011\u0000XV\u0001"+
		"\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000Y\t\u0001\u0000\u0000\u0000"+
		"Z[\u0005\t\u0000\u0000[\\\u0003$\u0012\u0000\\\u000b\u0001\u0000\u0000"+
		"\u0000]^\u0005\n\u0000\u0000^_\u0005)\u0000\u0000_`\u0005\'\u0000\u0000"+
		"`\r\u0001\u0000\u0000\u0000ab\u0005\u000b\u0000\u0000bc\u0003\"\u0011"+
		"\u0000cd\u0005\u0016\u0000\u0000dj\u0005*\u0000\u0000ef\u0003\u0002\u0001"+
		"\u0000fg\u0005*\u0000\u0000gi\u0001\u0000\u0000\u0000he\u0001\u0000\u0000"+
		"\u0000il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000"+
		"\u0000\u0000kw\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000mn\u0005"+
		"\f\u0000\u0000nt\u0005*\u0000\u0000op\u0003\u0002\u0001\u0000pq\u0005"+
		"*\u0000\u0000qs\u0001\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000sv\u0001"+
		"\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000"+
		"ux\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000wm\u0001\u0000\u0000"+
		"\u0000wx\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000yz\u0005\u0015"+
		"\u0000\u0000z\u000f\u0001\u0000\u0000\u0000{|\u0005\r\u0000\u0000|}\u0005"+
		"\'\u0000\u0000}~\u0005\"\u0000\u0000~\u007f\u0003$\u0012\u0000\u007f\u0080"+
		"\u0005\u000e\u0000\u0000\u0080\u0081\u0003$\u0012\u0000\u0081\u0087\u0005"+
		"*\u0000\u0000\u0082\u0083\u0003\u0002\u0001\u0000\u0083\u0084\u0005*\u0000"+
		"\u0000\u0084\u0086\u0001\u0000\u0000\u0000\u0085\u0082\u0001\u0000\u0000"+
		"\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000"+
		"\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008b\u0005\u000f\u0000"+
		"\u0000\u008b\u0011\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0010\u0000"+
		"\u0000\u008d\u008e\u0003\"\u0011\u0000\u008e\u0094\u0005*\u0000\u0000"+
		"\u008f\u0090\u0003\u0002\u0001\u0000\u0090\u0091\u0005*\u0000\u0000\u0091"+
		"\u0093\u0001\u0000\u0000\u0000\u0092\u008f\u0001\u0000\u0000\u0000\u0093"+
		"\u0096\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0001\u0000\u0000\u0000\u0095\u0097\u0001\u0000\u0000\u0000\u0096"+
		"\u0094\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u0015\u0000\u0000\u0098"+
		"\u0013\u0001\u0000\u0000\u0000\u0099\u009a\u0005\u0011\u0000\u0000\u009a"+
		"\u00a0\u0005*\u0000\u0000\u009b\u009c\u0003\u0002\u0001\u0000\u009c\u009d"+
		"\u0005*\u0000\u0000\u009d\u009f\u0001\u0000\u0000\u0000\u009e\u009b\u0001"+
		"\u0000\u0000\u0000\u009f\u00a2\u0001\u0000\u0000\u0000\u00a0\u009e\u0001"+
		"\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a3\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005"+
		"\u0012\u0000\u0000\u00a4\u00a5\u0003\"\u0011\u0000\u00a5\u0015\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a9\u0005\u0013\u0000\u0000\u00a7\u00a9\u0005\u0014"+
		"\u0000\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a8\u00a7\u0001\u0000"+
		"\u0000\u0000\u00a9\u0017\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005\u001c"+
		"\u0000\u0000\u00ab\u00ac\u0005\'\u0000\u0000\u00ac\u00ad\u0005\u0001\u0000"+
		"\u0000\u00ad\u00ae\u0003$\u0012\u0000\u00ae\u00af\u0005\u0002\u0000\u0000"+
		"\u00af\u0019\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u001d\u0000\u0000"+
		"\u00b1\u00b2\u0005\'\u0000\u0000\u00b2\u00b3\u0005\u0001\u0000\u0000\u00b3"+
		"\u00b4\u0003$\u0012\u0000\u00b4\u00b5\u0005\u0002\u0000\u0000\u00b5\u001b"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b7\u0007\u0000\u0000\u0000\u00b7\u001d"+
		"\u0001\u0000\u0000\u0000\u00b8\u00b9\u0007\u0001\u0000\u0000\u00b9\u001f"+
		"\u0001\u0000\u0000\u0000\u00ba\u00c0\u0005#\u0000\u0000\u00bb\u00c0\u0005"+
		"$\u0000\u0000\u00bc\u00c0\u0005%\u0000\u0000\u00bd\u00c0\u0005&\u0000"+
		"\u0000\u00be\u00c0\u0005\u0017\u0000\u0000\u00bf\u00ba\u0001\u0000\u0000"+
		"\u0000\u00bf\u00bb\u0001\u0000\u0000\u0000\u00bf\u00bc\u0001\u0000\u0000"+
		"\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00be\u0001\u0000\u0000"+
		"\u0000\u00c0!\u0001\u0000\u0000\u0000\u00c1\u00c2\u0003$\u0012\u0000\u00c2"+
		"\u00c3\u0003\u001e\u000f\u0000\u00c3\u00c4\u0003$\u0012\u0000\u00c4\u00cd"+
		"\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\u0005\u0000\u0000\u00c6\u00cd"+
		"\u0003\"\u0011\u0000\u00c7\u00c8\u0003$\u0012\u0000\u00c8\u00c9\u0003"+
		"\u001c\u000e\u0000\u00c9\u00ca\u0003\"\u0011\u0000\u00ca\u00cd\u0001\u0000"+
		"\u0000\u0000\u00cb\u00cd\u0003$\u0012\u0000\u00cc\u00c1\u0001\u0000\u0000"+
		"\u0000\u00cc\u00c5\u0001\u0000\u0000\u0000\u00cc\u00c7\u0001\u0000\u0000"+
		"\u0000\u00cc\u00cb\u0001\u0000\u0000\u0000\u00cd#\u0001\u0000\u0000\u0000"+
		"\u00ce\u00cf\u0006\u0012\uffff\uffff\u0000\u00cf\u00d0\u0005\u0003\u0000"+
		"\u0000\u00d0\u00d1\u0003$\u0012\u0000\u00d1\u00d2\u0005\u0004\u0000\u0000"+
		"\u00d2\u00dd\u0001\u0000\u0000\u0000\u00d3\u00dd\u0003&\u0013\u0000\u00d4"+
		"\u00dd\u0005(\u0000\u0000\u00d5\u00dd\u0005)\u0000\u0000\u00d6\u00dd\u0005"+
		"\'\u0000\u0000\u00d7\u00d8\u0005\'\u0000\u0000\u00d8\u00d9\u0005\u0001"+
		"\u0000\u0000\u00d9\u00da\u0003$\u0012\u0000\u00da\u00db\u0005\u0002\u0000"+
		"\u0000\u00db\u00dd\u0001\u0000\u0000\u0000\u00dc\u00ce\u0001\u0000\u0000"+
		"\u0000\u00dc\u00d3\u0001\u0000\u0000\u0000\u00dc\u00d4\u0001\u0000\u0000"+
		"\u0000\u00dc\u00d5\u0001\u0000\u0000\u0000\u00dc\u00d6\u0001\u0000\u0000"+
		"\u0000\u00dc\u00d7\u0001\u0000\u0000\u0000\u00dd\u00e4\u0001\u0000\u0000"+
		"\u0000\u00de\u00df\n\u0007\u0000\u0000\u00df\u00e0\u0003 \u0010\u0000"+
		"\u00e0\u00e1\u0003$\u0012\b\u00e1\u00e3\u0001\u0000\u0000\u0000\u00e2"+
		"\u00de\u0001\u0000\u0000\u0000\u00e3\u00e6\u0001\u0000\u0000\u0000\u00e4"+
		"\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5"+
		"%\u0001\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000\u00e7\u00e8"+
		"\u0005\u0018\u0000\u0000\u00e8\u00e9\u0005\u0003\u0000\u0000\u00e9\u00ea"+
		"\u0003$\u0012\u0000\u00ea\u00eb\u0005\u0004\u0000\u0000\u00eb\u00f7\u0001"+
		"\u0000\u0000\u0000\u00ec\u00ed\u0005\u0019\u0000\u0000\u00ed\u00ee\u0005"+
		"\u0003\u0000\u0000\u00ee\u00ef\u0003$\u0012\u0000\u00ef\u00f0\u0005\u0004"+
		"\u0000\u0000\u00f0\u00f7\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\u001a"+
		"\u0000\u0000\u00f2\u00f3\u0005\u0003\u0000\u0000\u00f3\u00f4\u0003$\u0012"+
		"\u0000\u00f4\u00f5\u0005\u0004\u0000\u0000\u00f5\u00f7\u0001\u0000\u0000"+
		"\u0000\u00f6\u00e7\u0001\u0000\u0000\u0000\u00f6\u00ec\u0001\u0000\u0000"+
		"\u0000\u00f6\u00f1\u0001\u0000\u0000\u0000\u00f7\'\u0001\u0000\u0000\u0000"+
		"\u0012,04DOXjtw\u0087\u0094\u00a0\u00a8\u00bf\u00cc\u00dc\u00e4\u00f6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}