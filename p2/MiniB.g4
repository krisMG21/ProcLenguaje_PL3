grammar MiniB;
// PARSER RULES
program:    (statement NEWLINE+)* statement? EOF
            ;

statement:  letStmt
            | opStmt
            | arrayOpStmt
            | printStmt
            | inputStmt
            | ifStmt
            | forStmt
            | whileStmt
            | repeatStmt
            | keyStmt
            | dimStmt
            | redimStmt
            | functionDefStmt
            ;

letStmt:    LET ID '=' exp=expression #Let
            ;

opStmt:     ID '=' (exp=expression | cond=condition) #Op
            ;
arrayOpStmt: ID '[' exp1=expression ']' '=' (exp2=expression | cond=condition) #ArrayOp
            ;

printStmt:  PRINT exp=expression #Print
            ;

inputStmt:  INPUT str=STRING_LITERAL ID #Input
            ;

ifStmt:     IF cond=condition THEN NEWLINE (statif=statement NEWLINE)*
            (ELSE NEWLINE (statelse=statement NEWLINE)*)? END #If
            ;

forStmt:    FOR ID '=' exp1=expression TO exp2=expression NEWLINE
            (stat=statement NEWLINE)* NEXT #For
            ;

whileStmt:  WHILE cond=condition NEWLINE (stat=statement NEWLINE)* END #While
            ;

repeatStmt: REPEAT NEWLINE (stat=statement NEWLINE)* UNTIL cond=condition #Repeat
            ;

keyStmt:    CONTINUE #Continue
            | EXIT #Exit
            ;

dimStmt:    DIM ID '[' exp=expression ']' #Dim
            ;

redimStmt:  REDIM ID '[' exp=expression ']' #Redim
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


arithmeticOp: PLUS  #PlusOperation
            | MINUS #MinusOperation
            | MUL   #MulOperation
            | DIV   #DivOperation
            | MOD   #ModOperation
            ;

condition:  left=expression op=comparisonOp right=expression #Comparison
            | NOT cond=condition #Not
            | left=expression op=logicalOp right=condition #Logical
            | expr=expression #condExp
            ;

expression: left=expression op=arithmeticOp right=expression #ArithmeticExpression
            | '(' expr=expression ')'    #ParenExpression
            | fun=functionCall      #FunctionCallExpression
            | NUMBER            #NumberExpression
            | STRING_LITERAL    #StringExpression
            | ID                 #IdExpression
            | ID '[' expr=expression ']' #ArrayAccessExpression
            ;

functionDefStmt: DEF ftype=TYPE name=ID '(' (ptypes=TYPE params=ID (','ptypes=TYPE params=ID)*)? ')'
            '{'
                 (stat=statement NEWLINE)* stat=statement?
            '}' #FunctionDef
            ;

functionCall: VAL '(' expr=expression ')'   #ValFunction
            | LEN '(' expr=expression ')'   #LenFunction
            | ISNAN '(' expr=expression ')' #IsNanFunction
            | name=ID '(' (expr=expression (',' expr=expression)*)? ')' #GenericFunction
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
REM:        'REM' | 'rem' ;
DIM:        'DIM' | 'dim' ;
REDIM:      'REDIM' | 'redim' ;
DEF:        'DEF' | 'def' ;
TYPE:       'INT' | 'int' | 'FLOAT' | 'float' | 'STRING' | 'string' | 'LIST' | 'list' | 'BOOLEAN' | 'boolean' ;

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
NUMBER: ('0x' [0-9a-fA-F]+ ('.' [0-9a-fA-F]+)?)
      | ('0b' [01]+ ('.' [01]+)?)
      | ('0o' [0-7]+ ('.' [0-7]+)?)
      | ([0-9]+ ('.' [0-9]+)?)
      ;

STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE:    '\r'? '\n';
COMMENT:    REM ~[\r\n]* NEWLINE*-> skip;
WS:         [ \t]+ -> skip;
