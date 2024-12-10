grammar BasicMejorado;
// PARSER RULES
program:        (statement NEWLINE+)* statement? EOF;
statement:  letStmt       #Let
            | opStmt        #Op
            | printStmt     #Print
            | inputStmt     #Input
            | ifStmt        #If
            | forStmt       #For
            | whileStmt     #While
            | repeatStmt    #Repeat
            | keyStmt       #Key
            ;


letStmt:    LET ID '=' exp=expression #Let
            ;

opStmt:     ID '=' esxp=expression    #Op
            ;

printStmt:  PRINT exp=expression    #Print
            ;

inputStmt:  INPUT STRING_LITERAL ID
            ;


ifStmt:     IF cond1=condition THEN NEWLINE (stat1=statement NEWLINE)* 
            (ELSE NEWLINE (stat2=statement NEWLINE)*)? END
            ;

forStmt:    FOR ID '=' exp1=expression TO exp2=expression NEWLINE (stat=statement NEWLINE)* NEXT
            ;

whileStmt:  WHILE condition NEWLINE (statement NEWLINE)* END;

repeatStmt: REPEAT NEWLINE (statement NEWLINE)* UNTIL condition;

keyStmt:    CONTINUE | EXIT;

condition:  expression comparisonOp expression 
            | NOT condition 
            | condition logicalOp condition 
            | expression
            ;

logicalOp: AND | OR;

comparisonOp:   '<' | '>' | '<=' | '>=' | '=';

expression:     expression op expression | '(' expression ')'  | functionCall | NUMBER | STRING_LITERAL | ID;

op:             '+' | '-' | '*' | '/' | MOD;

functionCall :  VAL '(' expression ')' | LEN '(' expression ')' | ISNAN '(' expression ')';


// LEXER RULES
NOT : 'NOT' | 'not';
AND: 'AND' | 'and';
OR: 'OR' | 'or';
LET : 'LET' | 'let';
PRINT : 'PRINT' | 'print' ;
INPUT : 'INPUT' | 'input' ;
IF : 'IF' | 'if' ;
ELSE : 'ELSE' | 'else' ;
FOR : 'FOR' | 'for' ;
TO : 'TO' | 'to' ;
NEXT : 'NEXT' | 'next' ;
WHILE : 'WHILE' | 'while' ;
REPEAT : 'REPEAT' | 'repeat' ;
UNTIL : 'UNTIL' | 'until' ;
CONTINUE : 'CONTINUE' | 'continue' ;
EXIT : 'EXIT' | 'exit' ;
END : 'END' | 'end' ;
THEN : 'THEN' | 'then' ;
MOD : 'MOD' | 'mod' ;
VAL : 'VAL' | 'val' ;
LEN : 'LEN' | 'len' ;
ISNAN : 'ISNAN' | 'isnan' ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
COMMENT: 'REM' ~[\r\n]* NEWLINE -> skip;
WS: [ \t]+ -> skip;
