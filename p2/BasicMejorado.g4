grammar BasicMejorado;
// PARSER RULES
program: (statement NEWLINE+)* statement? EOF;

statement:  letStmt #Let
            | opStmt #Op
            | printStmt #Print
            | inputStmt #Input
            | ifStmt #If
            | forStmt #For
            | whileStmt #While
            | repeatStmt #Repeat
            | keyStmt #Key
            ;

letStmt:    LET ID '=' exp=expression #Let
            ;

opStmt:     ID '=' exp=expression #Op
            ;

printStmt:  PRINT exp=expression #Print
            ;

inputStmt:  INPUT STRING_LITERAL ID #Input
            ;

ifStmt:     IF cond1=condition THEN NEWLINE (stat1=statement NEWLINE)*
            (ELSE NEWLINE (stat2=statement NEWLINE)*)? END #If
            ;

forStmt:    FOR ID '=' exp1=expression TO exp2=expression NEWLINE
            (stat=statement NEWLINE)* NEXT #For
            ;

whileStmt:  WHILE condition NEWLINE (statement NEWLINE)* END #While
            ;

repeatStmt: REPEAT NEWLINE (statement NEWLINE)* UNTIL condition #Repeat
            ;

keyStmt:    CONTINUE #Continue
            | EXIT #Exit
            | NOT condition #NotCondition
            | condition logicalOp condition #LogicalCondition
            | expression #ExpressionCondition
            ;

logicalOp:  AND #And
            | OR #Or
            | '>' #GreaterThan
            | '<=' #LessThanOrEqual
            | '>=' #GreaterThanOrEqual
            | '=' #Equal;

expression: expression op expression #BinaryExpression
            | '(' expression ')' #ParenExpression
            | functionCall #FunctionCallExpression
            | NUMBER #NumberExpression
            | STRING_LITERAL #StringExpression
            | ID #IdExpression;

op:         '+' #Plus
            | '-' #Minus
            | '*' #Multiply
            | '/' #Divide
            | MOD #Modulo
            ;

functionCall: VAL '(' expression ')' #ValFunction
            | LEN '(' expression ')' #LenFunction
            | ISNAN '(' expression ')' #IsNanFunction

// LEXER RULES
NOT:        'NOT' | 'not';
AND:        'AND' | 'and';
OR:         'OR' | 'or';
LET:        'LET' | 'let';
PRINT:      'PRINT' | 'print' ;
INPUT:      'INPUT' | 'input' ;
IF:         'IF' | 'if' ;
ELSE:       'ELSE' | 'else' ;
FOR:        'FOR' | 'for' ;
TO:         'TO' | 'to' ;
NEXT:       'NEXT' | 'next' ;
WHILE:      'WHILE' | 'while' ;
REPEAT:     'REPEAT' | 'repeat' ;
UNTIL:      'UNTIL' | 'until' ;
CONTINUE:   'CONTINUE' | 'continue' ;
EXIT:       'EXIT' | 'exit' ;
END:        'END' | 'end' ;
THEN:       'THEN' | 'then' ;
MOD:        'MOD' | 'mod' | '%';
VAL:        'VAL' | 'val' ;
LEN:        'LEN' | 'len' ;
ISNAN:      'ISNAN' | 'isnan' ;

ID:         [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER:     [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE:    '\r'? '\n';
COMMENT:    'REM' ~[\r\n]* NEWLINE -> skip;
WS:         [ \t]+ -> skip;
