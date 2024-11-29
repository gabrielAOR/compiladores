grammar Desenhar;

program: statement+ EOF;

statement
    : move
    | turn
    | pen
    | color
    | repeat
    ;

move: 'MOVE' INT ';' ;
turn: 'TURN' INT ';' ;
pen: ('PENUP' | 'PENDOWN') ';' ;
color: 'COLOR' COLOR ';' ;
repeat: 'REPEAT' INT '{' statement+ '}' ;

COLOR: 'RED' | 'GREEN' | 'BLUE' | 'BLACK' | 'YELLOW' ;
INT: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;