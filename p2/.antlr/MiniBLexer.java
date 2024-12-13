// Generated from c:/Users/ruben/Desktop/Uni/4/Lenguaje/ProcLenguaje_PL3/p2/MiniB.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MiniBLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "NOT", "AND", "OR", "LET", "PRINT", "INPUT", 
			"IF", "ELSE", "FOR", "TO", "NEXT", "WHILE", "REPEAT", "UNTIL", "CONTINUE", 
			"EXIT", "END", "THEN", "MOD", "VAL", "LEN", "ISNAN", "REM", "DIM", "REDIM", 
			"LT", "GT", "LE", "GE", "EQ", "PLUS", "MINUS", "MUL", "DIV", "ID", "NUMBER", 
			"STRING_LITERAL", "NEWLINE", "COMMENT", "WS"
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


	public MiniBLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiniB.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000,\u01d5\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004h\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005p\b\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006v\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007~\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u008a\b\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0096"+
		"\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u009c\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u00a6\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\f\u00ae\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00b4"+
		"\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00be\b\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00ca\b\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00d8"+
		"\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00e4"+
		"\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00f6"+
		"\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u0100\b\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u0108"+
		"\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0112\b\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003"+
		"\u0016\u011b\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0003\u0017\u0123\b\u0017\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u012b\b\u0018\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0137\b\u0019\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003"+
		"\u001a\u013f\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0003\u001b\u0147\b\u001b\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0003\u001c\u0153\b\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001"+
		" \u0001!\u0001!\u0001\"\u0001\"\u0001#\u0001#\u0001$\u0001$\u0001%\u0001"+
		"%\u0001&\u0001&\u0005&\u016b\b&\n&\f&\u016e\t&\u0001\'\u0001\'\u0001\'"+
		"\u0001\'\u0004\'\u0174\b\'\u000b\'\f\'\u0175\u0001\'\u0001\'\u0004\'\u017a"+
		"\b\'\u000b\'\f\'\u017b\u0003\'\u017e\b\'\u0001\'\u0001\'\u0001\'\u0001"+
		"\'\u0004\'\u0184\b\'\u000b\'\f\'\u0185\u0001\'\u0001\'\u0004\'\u018a\b"+
		"\'\u000b\'\f\'\u018b\u0003\'\u018e\b\'\u0001\'\u0001\'\u0001\'\u0001\'"+
		"\u0004\'\u0194\b\'\u000b\'\f\'\u0195\u0001\'\u0001\'\u0004\'\u019a\b\'"+
		"\u000b\'\f\'\u019b\u0003\'\u019e\b\'\u0001\'\u0004\'\u01a1\b\'\u000b\'"+
		"\f\'\u01a2\u0001\'\u0001\'\u0004\'\u01a7\b\'\u000b\'\f\'\u01a8\u0003\'"+
		"\u01ab\b\'\u0003\'\u01ad\b\'\u0001(\u0001(\u0005(\u01b1\b(\n(\f(\u01b4"+
		"\t(\u0001(\u0001(\u0001)\u0003)\u01b9\b)\u0001)\u0001)\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0003*\u01c3\b*\u0001*\u0005*\u01c6\b*\n*\f*\u01c9"+
		"\t*\u0001*\u0001*\u0001*\u0001*\u0001+\u0004+\u01d0\b+\u000b+\f+\u01d1"+
		"\u0001+\u0001+\u0000\u0000,\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013"+
		"\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d"+
		";\u001e=\u001f? A!C\"E#G$I%K&M\'O(Q)S*U+W,\u0001\u0000\t\u0003\u0000A"+
		"Z__az\u0004\u000009AZ__az\u0003\u000009AFaf\u0001\u000001\u0001\u0000"+
		"07\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000\n\n\r\r  \u0002\u0000"+
		"\t\t  \u0203\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000"+
		"A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001"+
		"\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000"+
		"\u0000\u0000K\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000\u0000\u0000"+
		"O\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000\u0000\u0000\u0000S\u0001"+
		"\u0000\u0000\u0000\u0000U\u0001\u0000\u0000\u0000\u0000W\u0001\u0000\u0000"+
		"\u0000\u0001Y\u0001\u0000\u0000\u0000\u0003[\u0001\u0000\u0000\u0000\u0005"+
		"]\u0001\u0000\u0000\u0000\u0007_\u0001\u0000\u0000\u0000\tg\u0001\u0000"+
		"\u0000\u0000\u000bo\u0001\u0000\u0000\u0000\ru\u0001\u0000\u0000\u0000"+
		"\u000f}\u0001\u0000\u0000\u0000\u0011\u0089\u0001\u0000\u0000\u0000\u0013"+
		"\u0095\u0001\u0000\u0000\u0000\u0015\u009b\u0001\u0000\u0000\u0000\u0017"+
		"\u00a5\u0001\u0000\u0000\u0000\u0019\u00ad\u0001\u0000\u0000\u0000\u001b"+
		"\u00b3\u0001\u0000\u0000\u0000\u001d\u00bd\u0001\u0000\u0000\u0000\u001f"+
		"\u00c9\u0001\u0000\u0000\u0000!\u00d7\u0001\u0000\u0000\u0000#\u00e3\u0001"+
		"\u0000\u0000\u0000%\u00f5\u0001\u0000\u0000\u0000\'\u00ff\u0001\u0000"+
		"\u0000\u0000)\u0107\u0001\u0000\u0000\u0000+\u0111\u0001\u0000\u0000\u0000"+
		"-\u011a\u0001\u0000\u0000\u0000/\u0122\u0001\u0000\u0000\u00001\u012a"+
		"\u0001\u0000\u0000\u00003\u0136\u0001\u0000\u0000\u00005\u013e\u0001\u0000"+
		"\u0000\u00007\u0146\u0001\u0000\u0000\u00009\u0152\u0001\u0000\u0000\u0000"+
		";\u0154\u0001\u0000\u0000\u0000=\u0156\u0001\u0000\u0000\u0000?\u0158"+
		"\u0001\u0000\u0000\u0000A\u015b\u0001\u0000\u0000\u0000C\u015e\u0001\u0000"+
		"\u0000\u0000E\u0160\u0001\u0000\u0000\u0000G\u0162\u0001\u0000\u0000\u0000"+
		"I\u0164\u0001\u0000\u0000\u0000K\u0166\u0001\u0000\u0000\u0000M\u0168"+
		"\u0001\u0000\u0000\u0000O\u01ac\u0001\u0000\u0000\u0000Q\u01ae\u0001\u0000"+
		"\u0000\u0000S\u01b8\u0001\u0000\u0000\u0000U\u01c2\u0001\u0000\u0000\u0000"+
		"W\u01cf\u0001\u0000\u0000\u0000YZ\u0005[\u0000\u0000Z\u0002\u0001\u0000"+
		"\u0000\u0000[\\\u0005]\u0000\u0000\\\u0004\u0001\u0000\u0000\u0000]^\u0005"+
		"(\u0000\u0000^\u0006\u0001\u0000\u0000\u0000_`\u0005)\u0000\u0000`\b\u0001"+
		"\u0000\u0000\u0000ab\u0005N\u0000\u0000bc\u0005O\u0000\u0000ch\u0005T"+
		"\u0000\u0000de\u0005n\u0000\u0000ef\u0005o\u0000\u0000fh\u0005t\u0000"+
		"\u0000ga\u0001\u0000\u0000\u0000gd\u0001\u0000\u0000\u0000h\n\u0001\u0000"+
		"\u0000\u0000ij\u0005A\u0000\u0000jk\u0005N\u0000\u0000kp\u0005D\u0000"+
		"\u0000lm\u0005a\u0000\u0000mn\u0005n\u0000\u0000np\u0005d\u0000\u0000"+
		"oi\u0001\u0000\u0000\u0000ol\u0001\u0000\u0000\u0000p\f\u0001\u0000\u0000"+
		"\u0000qr\u0005O\u0000\u0000rv\u0005R\u0000\u0000st\u0005o\u0000\u0000"+
		"tv\u0005r\u0000\u0000uq\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000"+
		"v\u000e\u0001\u0000\u0000\u0000wx\u0005L\u0000\u0000xy\u0005E\u0000\u0000"+
		"y~\u0005T\u0000\u0000z{\u0005l\u0000\u0000{|\u0005e\u0000\u0000|~\u0005"+
		"t\u0000\u0000}w\u0001\u0000\u0000\u0000}z\u0001\u0000\u0000\u0000~\u0010"+
		"\u0001\u0000\u0000\u0000\u007f\u0080\u0005P\u0000\u0000\u0080\u0081\u0005"+
		"R\u0000\u0000\u0081\u0082\u0005I\u0000\u0000\u0082\u0083\u0005N\u0000"+
		"\u0000\u0083\u008a\u0005T\u0000\u0000\u0084\u0085\u0005p\u0000\u0000\u0085"+
		"\u0086\u0005r\u0000\u0000\u0086\u0087\u0005i\u0000\u0000\u0087\u0088\u0005"+
		"n\u0000\u0000\u0088\u008a\u0005t\u0000\u0000\u0089\u007f\u0001\u0000\u0000"+
		"\u0000\u0089\u0084\u0001\u0000\u0000\u0000\u008a\u0012\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0005I\u0000\u0000\u008c\u008d\u0005N\u0000\u0000\u008d"+
		"\u008e\u0005P\u0000\u0000\u008e\u008f\u0005U\u0000\u0000\u008f\u0096\u0005"+
		"T\u0000\u0000\u0090\u0091\u0005i\u0000\u0000\u0091\u0092\u0005n\u0000"+
		"\u0000\u0092\u0093\u0005p\u0000\u0000\u0093\u0094\u0005u\u0000\u0000\u0094"+
		"\u0096\u0005t\u0000\u0000\u0095\u008b\u0001\u0000\u0000\u0000\u0095\u0090"+
		"\u0001\u0000\u0000\u0000\u0096\u0014\u0001\u0000\u0000\u0000\u0097\u0098"+
		"\u0005I\u0000\u0000\u0098\u009c\u0005F\u0000\u0000\u0099\u009a\u0005i"+
		"\u0000\u0000\u009a\u009c\u0005f\u0000\u0000\u009b\u0097\u0001\u0000\u0000"+
		"\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009c\u0016\u0001\u0000\u0000"+
		"\u0000\u009d\u009e\u0005E\u0000\u0000\u009e\u009f\u0005L\u0000\u0000\u009f"+
		"\u00a0\u0005S\u0000\u0000\u00a0\u00a6\u0005E\u0000\u0000\u00a1\u00a2\u0005"+
		"e\u0000\u0000\u00a2\u00a3\u0005l\u0000\u0000\u00a3\u00a4\u0005s\u0000"+
		"\u0000\u00a4\u00a6\u0005e\u0000\u0000\u00a5\u009d\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a1\u0001\u0000\u0000\u0000\u00a6\u0018\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a8\u0005F\u0000\u0000\u00a8\u00a9\u0005O\u0000\u0000\u00a9\u00ae"+
		"\u0005R\u0000\u0000\u00aa\u00ab\u0005f\u0000\u0000\u00ab\u00ac\u0005o"+
		"\u0000\u0000\u00ac\u00ae\u0005r\u0000\u0000\u00ad\u00a7\u0001\u0000\u0000"+
		"\u0000\u00ad\u00aa\u0001\u0000\u0000\u0000\u00ae\u001a\u0001\u0000\u0000"+
		"\u0000\u00af\u00b0\u0005T\u0000\u0000\u00b0\u00b4\u0005O\u0000\u0000\u00b1"+
		"\u00b2\u0005t\u0000\u0000\u00b2\u00b4\u0005o\u0000\u0000\u00b3\u00af\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000\u00b4\u001c\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b6\u0005N\u0000\u0000\u00b6\u00b7\u0005E\u0000"+
		"\u0000\u00b7\u00b8\u0005X\u0000\u0000\u00b8\u00be\u0005T\u0000\u0000\u00b9"+
		"\u00ba\u0005n\u0000\u0000\u00ba\u00bb\u0005e\u0000\u0000\u00bb\u00bc\u0005"+
		"x\u0000\u0000\u00bc\u00be\u0005t\u0000\u0000\u00bd\u00b5\u0001\u0000\u0000"+
		"\u0000\u00bd\u00b9\u0001\u0000\u0000\u0000\u00be\u001e\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c0\u0005W\u0000\u0000\u00c0\u00c1\u0005H\u0000\u0000\u00c1"+
		"\u00c2\u0005I\u0000\u0000\u00c2\u00c3\u0005L\u0000\u0000\u00c3\u00ca\u0005"+
		"E\u0000\u0000\u00c4\u00c5\u0005w\u0000\u0000\u00c5\u00c6\u0005h\u0000"+
		"\u0000\u00c6\u00c7\u0005i\u0000\u0000\u00c7\u00c8\u0005l\u0000\u0000\u00c8"+
		"\u00ca\u0005e\u0000\u0000\u00c9\u00bf\u0001\u0000\u0000\u0000\u00c9\u00c4"+
		"\u0001\u0000\u0000\u0000\u00ca \u0001\u0000\u0000\u0000\u00cb\u00cc\u0005"+
		"R\u0000\u0000\u00cc\u00cd\u0005E\u0000\u0000\u00cd\u00ce\u0005P\u0000"+
		"\u0000\u00ce\u00cf\u0005E\u0000\u0000\u00cf\u00d0\u0005A\u0000\u0000\u00d0"+
		"\u00d8\u0005T\u0000\u0000\u00d1\u00d2\u0005r\u0000\u0000\u00d2\u00d3\u0005"+
		"e\u0000\u0000\u00d3\u00d4\u0005p\u0000\u0000\u00d4\u00d5\u0005e\u0000"+
		"\u0000\u00d5\u00d6\u0005a\u0000\u0000\u00d6\u00d8\u0005t\u0000\u0000\u00d7"+
		"\u00cb\u0001\u0000\u0000\u0000\u00d7\u00d1\u0001\u0000\u0000\u0000\u00d8"+
		"\"\u0001\u0000\u0000\u0000\u00d9\u00da\u0005U\u0000\u0000\u00da\u00db"+
		"\u0005N\u0000\u0000\u00db\u00dc\u0005T\u0000\u0000\u00dc\u00dd\u0005I"+
		"\u0000\u0000\u00dd\u00e4\u0005L\u0000\u0000\u00de\u00df\u0005u\u0000\u0000"+
		"\u00df\u00e0\u0005n\u0000\u0000\u00e0\u00e1\u0005t\u0000\u0000\u00e1\u00e2"+
		"\u0005i\u0000\u0000\u00e2\u00e4\u0005l\u0000\u0000\u00e3\u00d9\u0001\u0000"+
		"\u0000\u0000\u00e3\u00de\u0001\u0000\u0000\u0000\u00e4$\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e6\u0005C\u0000\u0000\u00e6\u00e7\u0005O\u0000\u0000\u00e7"+
		"\u00e8\u0005N\u0000\u0000\u00e8\u00e9\u0005T\u0000\u0000\u00e9\u00ea\u0005"+
		"I\u0000\u0000\u00ea\u00eb\u0005N\u0000\u0000\u00eb\u00ec\u0005U\u0000"+
		"\u0000\u00ec\u00f6\u0005E\u0000\u0000\u00ed\u00ee\u0005c\u0000\u0000\u00ee"+
		"\u00ef\u0005o\u0000\u0000\u00ef\u00f0\u0005n\u0000\u0000\u00f0\u00f1\u0005"+
		"t\u0000\u0000\u00f1\u00f2\u0005i\u0000\u0000\u00f2\u00f3\u0005n\u0000"+
		"\u0000\u00f3\u00f4\u0005u\u0000\u0000\u00f4\u00f6\u0005e\u0000\u0000\u00f5"+
		"\u00e5\u0001\u0000\u0000\u0000\u00f5\u00ed\u0001\u0000\u0000\u0000\u00f6"+
		"&\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005E\u0000\u0000\u00f8\u00f9\u0005"+
		"X\u0000\u0000\u00f9\u00fa\u0005I\u0000\u0000\u00fa\u0100\u0005T\u0000"+
		"\u0000\u00fb\u00fc\u0005e\u0000\u0000\u00fc\u00fd\u0005x\u0000\u0000\u00fd"+
		"\u00fe\u0005i\u0000\u0000\u00fe\u0100\u0005t\u0000\u0000\u00ff\u00f7\u0001"+
		"\u0000\u0000\u0000\u00ff\u00fb\u0001\u0000\u0000\u0000\u0100(\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0005E\u0000\u0000\u0102\u0103\u0005N\u0000\u0000"+
		"\u0103\u0108\u0005D\u0000\u0000\u0104\u0105\u0005e\u0000\u0000\u0105\u0106"+
		"\u0005n\u0000\u0000\u0106\u0108\u0005d\u0000\u0000\u0107\u0101\u0001\u0000"+
		"\u0000\u0000\u0107\u0104\u0001\u0000\u0000\u0000\u0108*\u0001\u0000\u0000"+
		"\u0000\u0109\u010a\u0005T\u0000\u0000\u010a\u010b\u0005H\u0000\u0000\u010b"+
		"\u010c\u0005E\u0000\u0000\u010c\u0112\u0005N\u0000\u0000\u010d\u010e\u0005"+
		"t\u0000\u0000\u010e\u010f\u0005h\u0000\u0000\u010f\u0110\u0005e\u0000"+
		"\u0000\u0110\u0112\u0005n\u0000\u0000\u0111\u0109\u0001\u0000\u0000\u0000"+
		"\u0111\u010d\u0001\u0000\u0000\u0000\u0112,\u0001\u0000\u0000\u0000\u0113"+
		"\u0114\u0005M\u0000\u0000\u0114\u0115\u0005O\u0000\u0000\u0115\u011b\u0005"+
		"D\u0000\u0000\u0116\u0117\u0005m\u0000\u0000\u0117\u0118\u0005o\u0000"+
		"\u0000\u0118\u011b\u0005d\u0000\u0000\u0119\u011b\u0005%\u0000\u0000\u011a"+
		"\u0113\u0001\u0000\u0000\u0000\u011a\u0116\u0001\u0000\u0000\u0000\u011a"+
		"\u0119\u0001\u0000\u0000\u0000\u011b.\u0001\u0000\u0000\u0000\u011c\u011d"+
		"\u0005V\u0000\u0000\u011d\u011e\u0005A\u0000\u0000\u011e\u0123\u0005L"+
		"\u0000\u0000\u011f\u0120\u0005v\u0000\u0000\u0120\u0121\u0005a\u0000\u0000"+
		"\u0121\u0123\u0005l\u0000\u0000\u0122\u011c\u0001\u0000\u0000\u0000\u0122"+
		"\u011f\u0001\u0000\u0000\u0000\u01230\u0001\u0000\u0000\u0000\u0124\u0125"+
		"\u0005L\u0000\u0000\u0125\u0126\u0005E\u0000\u0000\u0126\u012b\u0005N"+
		"\u0000\u0000\u0127\u0128\u0005l\u0000\u0000\u0128\u0129\u0005e\u0000\u0000"+
		"\u0129\u012b\u0005n\u0000\u0000\u012a\u0124\u0001\u0000\u0000\u0000\u012a"+
		"\u0127\u0001\u0000\u0000\u0000\u012b2\u0001\u0000\u0000\u0000\u012c\u012d"+
		"\u0005I\u0000\u0000\u012d\u012e\u0005S\u0000\u0000\u012e\u012f\u0005N"+
		"\u0000\u0000\u012f\u0130\u0005A\u0000\u0000\u0130\u0137\u0005N\u0000\u0000"+
		"\u0131\u0132\u0005i\u0000\u0000\u0132\u0133\u0005s\u0000\u0000\u0133\u0134"+
		"\u0005n\u0000\u0000\u0134\u0135\u0005a\u0000\u0000\u0135\u0137\u0005n"+
		"\u0000\u0000\u0136\u012c\u0001\u0000\u0000\u0000\u0136\u0131\u0001\u0000"+
		"\u0000\u0000\u01374\u0001\u0000\u0000\u0000\u0138\u0139\u0005R\u0000\u0000"+
		"\u0139\u013a\u0005E\u0000\u0000\u013a\u013f\u0005M\u0000\u0000\u013b\u013c"+
		"\u0005r\u0000\u0000\u013c\u013d\u0005e\u0000\u0000\u013d\u013f\u0005m"+
		"\u0000\u0000\u013e\u0138\u0001\u0000\u0000\u0000\u013e\u013b\u0001\u0000"+
		"\u0000\u0000\u013f6\u0001\u0000\u0000\u0000\u0140\u0141\u0005D\u0000\u0000"+
		"\u0141\u0142\u0005I\u0000\u0000\u0142\u0147\u0005M\u0000\u0000\u0143\u0144"+
		"\u0005d\u0000\u0000\u0144\u0145\u0005i\u0000\u0000\u0145\u0147\u0005m"+
		"\u0000\u0000\u0146\u0140\u0001\u0000\u0000\u0000\u0146\u0143\u0001\u0000"+
		"\u0000\u0000\u01478\u0001\u0000\u0000\u0000\u0148\u0149\u0005R\u0000\u0000"+
		"\u0149\u014a\u0005E\u0000\u0000\u014a\u014b\u0005D\u0000\u0000\u014b\u014c"+
		"\u0005I\u0000\u0000\u014c\u0153\u0005M\u0000\u0000\u014d\u014e\u0005r"+
		"\u0000\u0000\u014e\u014f\u0005e\u0000\u0000\u014f\u0150\u0005d\u0000\u0000"+
		"\u0150\u0151\u0005i\u0000\u0000\u0151\u0153\u0005m\u0000\u0000\u0152\u0148"+
		"\u0001\u0000\u0000\u0000\u0152\u014d\u0001\u0000\u0000\u0000\u0153:\u0001"+
		"\u0000\u0000\u0000\u0154\u0155\u0005<\u0000\u0000\u0155<\u0001\u0000\u0000"+
		"\u0000\u0156\u0157\u0005>\u0000\u0000\u0157>\u0001\u0000\u0000\u0000\u0158"+
		"\u0159\u0005<\u0000\u0000\u0159\u015a\u0005=\u0000\u0000\u015a@\u0001"+
		"\u0000\u0000\u0000\u015b\u015c\u0005>\u0000\u0000\u015c\u015d\u0005=\u0000"+
		"\u0000\u015dB\u0001\u0000\u0000\u0000\u015e\u015f\u0005=\u0000\u0000\u015f"+
		"D\u0001\u0000\u0000\u0000\u0160\u0161\u0005+\u0000\u0000\u0161F\u0001"+
		"\u0000\u0000\u0000\u0162\u0163\u0005-\u0000\u0000\u0163H\u0001\u0000\u0000"+
		"\u0000\u0164\u0165\u0005*\u0000\u0000\u0165J\u0001\u0000\u0000\u0000\u0166"+
		"\u0167\u0005/\u0000\u0000\u0167L\u0001\u0000\u0000\u0000\u0168\u016c\u0007"+
		"\u0000\u0000\u0000\u0169\u016b\u0007\u0001\u0000\u0000\u016a\u0169\u0001"+
		"\u0000\u0000\u0000\u016b\u016e\u0001\u0000\u0000\u0000\u016c\u016a\u0001"+
		"\u0000\u0000\u0000\u016c\u016d\u0001\u0000\u0000\u0000\u016dN\u0001\u0000"+
		"\u0000\u0000\u016e\u016c\u0001\u0000\u0000\u0000\u016f\u0170\u00050\u0000"+
		"\u0000\u0170\u0171\u0005x\u0000\u0000\u0171\u0173\u0001\u0000\u0000\u0000"+
		"\u0172\u0174\u0007\u0002\u0000\u0000\u0173\u0172\u0001\u0000\u0000\u0000"+
		"\u0174\u0175\u0001\u0000\u0000\u0000\u0175\u0173\u0001\u0000\u0000\u0000"+
		"\u0175\u0176\u0001\u0000\u0000\u0000\u0176\u017d\u0001\u0000\u0000\u0000"+
		"\u0177\u0179\u0005.\u0000\u0000\u0178\u017a\u0007\u0002\u0000\u0000\u0179"+
		"\u0178\u0001\u0000\u0000\u0000\u017a\u017b\u0001\u0000\u0000\u0000\u017b"+
		"\u0179\u0001\u0000\u0000\u0000\u017b\u017c\u0001\u0000\u0000\u0000\u017c"+
		"\u017e\u0001\u0000\u0000\u0000\u017d\u0177\u0001\u0000\u0000\u0000\u017d"+
		"\u017e\u0001\u0000\u0000\u0000\u017e\u01ad\u0001\u0000\u0000\u0000\u017f"+
		"\u0180\u00050\u0000\u0000\u0180\u0181\u0005b\u0000\u0000\u0181\u0183\u0001"+
		"\u0000\u0000\u0000\u0182\u0184\u0007\u0003\u0000\u0000\u0183\u0182\u0001"+
		"\u0000\u0000\u0000\u0184\u0185\u0001\u0000\u0000\u0000\u0185\u0183\u0001"+
		"\u0000\u0000\u0000\u0185\u0186\u0001\u0000\u0000\u0000\u0186\u018d\u0001"+
		"\u0000\u0000\u0000\u0187\u0189\u0005.\u0000\u0000\u0188\u018a\u0007\u0003"+
		"\u0000\u0000\u0189\u0188\u0001\u0000\u0000\u0000\u018a\u018b\u0001\u0000"+
		"\u0000\u0000\u018b\u0189\u0001\u0000\u0000\u0000\u018b\u018c\u0001\u0000"+
		"\u0000\u0000\u018c\u018e\u0001\u0000\u0000\u0000\u018d\u0187\u0001\u0000"+
		"\u0000\u0000\u018d\u018e\u0001\u0000\u0000\u0000\u018e\u01ad\u0001\u0000"+
		"\u0000\u0000\u018f\u0190\u00050\u0000\u0000\u0190\u0191\u0005o\u0000\u0000"+
		"\u0191\u0193\u0001\u0000\u0000\u0000\u0192\u0194\u0007\u0004\u0000\u0000"+
		"\u0193\u0192\u0001\u0000\u0000\u0000\u0194\u0195\u0001\u0000\u0000\u0000"+
		"\u0195\u0193\u0001\u0000\u0000\u0000\u0195\u0196\u0001\u0000\u0000\u0000"+
		"\u0196\u019d\u0001\u0000\u0000\u0000\u0197\u0199\u0005.\u0000\u0000\u0198"+
		"\u019a\u0007\u0004\u0000\u0000\u0199\u0198\u0001\u0000\u0000\u0000\u019a"+
		"\u019b\u0001\u0000\u0000\u0000\u019b\u0199\u0001\u0000\u0000\u0000\u019b"+
		"\u019c\u0001\u0000\u0000\u0000\u019c\u019e\u0001\u0000\u0000\u0000\u019d"+
		"\u0197\u0001\u0000\u0000\u0000\u019d\u019e\u0001\u0000\u0000\u0000\u019e"+
		"\u01ad\u0001\u0000\u0000\u0000\u019f\u01a1\u0007\u0005\u0000\u0000\u01a0"+
		"\u019f\u0001\u0000\u0000\u0000\u01a1\u01a2\u0001\u0000\u0000\u0000\u01a2"+
		"\u01a0\u0001\u0000\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000\u0000\u01a3"+
		"\u01aa\u0001\u0000\u0000\u0000\u01a4\u01a6\u0005.\u0000\u0000\u01a5\u01a7"+
		"\u0007\u0005\u0000\u0000\u01a6\u01a5\u0001\u0000\u0000\u0000\u01a7\u01a8"+
		"\u0001\u0000\u0000\u0000\u01a8\u01a6\u0001\u0000\u0000\u0000\u01a8\u01a9"+
		"\u0001\u0000\u0000\u0000\u01a9\u01ab\u0001\u0000\u0000\u0000\u01aa\u01a4"+
		"\u0001\u0000\u0000\u0000\u01aa\u01ab\u0001\u0000\u0000\u0000\u01ab\u01ad"+
		"\u0001\u0000\u0000\u0000\u01ac\u016f\u0001\u0000\u0000\u0000\u01ac\u017f"+
		"\u0001\u0000\u0000\u0000\u01ac\u018f\u0001\u0000\u0000\u0000\u01ac\u01a0"+
		"\u0001\u0000\u0000\u0000\u01adP\u0001\u0000\u0000\u0000\u01ae\u01b2\u0005"+
		"\"\u0000\u0000\u01af\u01b1\b\u0006\u0000\u0000\u01b0\u01af\u0001\u0000"+
		"\u0000\u0000\u01b1\u01b4\u0001\u0000\u0000\u0000\u01b2\u01b0\u0001\u0000"+
		"\u0000\u0000\u01b2\u01b3\u0001\u0000\u0000\u0000\u01b3\u01b5\u0001\u0000"+
		"\u0000\u0000\u01b4\u01b2\u0001\u0000\u0000\u0000\u01b5\u01b6\u0005\"\u0000"+
		"\u0000\u01b6R\u0001\u0000\u0000\u0000\u01b7\u01b9\u0005\r\u0000\u0000"+
		"\u01b8\u01b7\u0001\u0000\u0000\u0000\u01b8\u01b9\u0001\u0000\u0000\u0000"+
		"\u01b9\u01ba\u0001\u0000\u0000\u0000\u01ba\u01bb\u0005\n\u0000\u0000\u01bb"+
		"T\u0001\u0000\u0000\u0000\u01bc\u01bd\u0005R\u0000\u0000\u01bd\u01be\u0005"+
		"E\u0000\u0000\u01be\u01c3\u0005M\u0000\u0000\u01bf\u01c0\u0005r\u0000"+
		"\u0000\u01c0\u01c1\u0005e\u0000\u0000\u01c1\u01c3\u0005m\u0000\u0000\u01c2"+
		"\u01bc\u0001\u0000\u0000\u0000\u01c2\u01bf\u0001\u0000\u0000\u0000\u01c3"+
		"\u01c7\u0001\u0000\u0000\u0000\u01c4\u01c6\b\u0007\u0000\u0000\u01c5\u01c4"+
		"\u0001\u0000\u0000\u0000\u01c6\u01c9\u0001\u0000\u0000\u0000\u01c7\u01c5"+
		"\u0001\u0000\u0000\u0000\u01c7\u01c8\u0001\u0000\u0000\u0000\u01c8\u01ca"+
		"\u0001\u0000\u0000\u0000\u01c9\u01c7\u0001\u0000\u0000\u0000\u01ca\u01cb"+
		"\u0003S)\u0000\u01cb\u01cc\u0001\u0000\u0000\u0000\u01cc\u01cd\u0006*"+
		"\u0000\u0000\u01cdV\u0001\u0000\u0000\u0000\u01ce\u01d0\u0007\b\u0000"+
		"\u0000\u01cf\u01ce\u0001\u0000\u0000\u0000\u01d0\u01d1\u0001\u0000\u0000"+
		"\u0000\u01d1\u01cf\u0001\u0000\u0000\u0000\u01d1\u01d2\u0001\u0000\u0000"+
		"\u0000\u01d2\u01d3\u0001\u0000\u0000\u0000\u01d3\u01d4\u0006+\u0000\u0000"+
		"\u01d4X\u0001\u0000\u0000\u0000-\u0000gou}\u0089\u0095\u009b\u00a5\u00ad"+
		"\u00b3\u00bd\u00c9\u00d7\u00e3\u00f5\u00ff\u0107\u0111\u011a\u0122\u012a"+
		"\u0136\u013e\u0146\u0152\u016c\u0175\u017b\u017d\u0185\u018b\u018d\u0195"+
		"\u019b\u019d\u01a2\u01a8\u01aa\u01ac\u01b2\u01b8\u01c2\u01c7\u01d1\u0001"+
		"\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}