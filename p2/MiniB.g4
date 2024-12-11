grammar MiniB;
// PARSER RULES
program:    (statement NEWLINE+)* statement? EOF
            ;

statement:  letStmt
            | opStmt
            | printStmt
            | inputStmt
            | ifStmt
            | forStmt
            | whileStmt
            | repeatStmt
            | keyStmt
            ;

letStmt:    LET id=ID '=' exp=expression #Let
            ;

opStmt:     id=ID '=' exp=expression #Op
            ;

printStmt:  PRINT exp=expression #Print
            ;

inputStmt:  INPUT str=STRING_LITERAL id=ID #Input
            ;

ifStmt:     IF cond=condition THEN NEWLINE (statif=statement NEWLINE)*
            (ELSE NEWLINE (statelse=statement NEWLINE)*)? END #If
            ;

forStmt:    FOR id=ID '=' exp1=expression TO exp2=expression NEWLINE
            (stat=statement NEWLINE)* NEXT #For
            ;

whileStmt:  WHILE cond=condition NEWLINE (stat=statement NEWLINE)* END #While
            ;

repeatStmt: REPEAT NEWLINE (stat=statement NEWLINE)* UNTIL cond=condition #Repeat
            ;

keyStmt:    CONTINUE #Continue
            | EXIT #Exit
            ;

logicalOp:  AND
            | OR
            ;

comparisonOp: LT
            | GT
            | LE
            | GE
            | EQ
            ;


arithmeticOp: PLUS
            | MINUS
            | MUL
            | DIV
            | MOD
            ;

condition:  left=expression op=comparisonOp right=expression #Comparison
            | NOT cond=condition #Not
            | left=condition op=logicalOp right=condition #Logical
            | expr=expression
            ;

expression: left=expression op=arithmeticOp right=expression #ArithmeticExpression
            | '(' expr=expression ')'    #ParenExpression
            | fun=functionCall      #FunctionCallExpression
            | NUMBER            #NumberExpression
            | STRING_LITERAL    #StringExpression
            | ID                 #IdExpression
            ;

functionCall: VAL '(' expr=expression ')'   #ValFunction
            | LEN '(' expr=expression ')'   #LenFunction
            | ISNAN '(' expr=expression ')' #IsNanFunction
            ;

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

LT:         '<' ;
GT:         '>' ;
LE:         '<=' ;
GE:         '>=' ;
EQ:         '=' ;

PLUS:       '+' ;
MINUS:      '-' ;
MUL:        '*' ;
DIV:        '/' ;

ID:         [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER:     [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE:    '\r'? '\n';
COMMENT:    'REM' ~[\r\n]* NEWLINE -> skip;
WS:         [ \t]+ -> skip;
