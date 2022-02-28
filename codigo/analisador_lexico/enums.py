import enum

class TOKEN_TIPO(enum.Enum):
    COMANDBREAK = 1
    OPENPARENT  = 2
    CLOSEPARENT = 3
    ID          = 4
    SE          = 5
    FIM         = 6
    CHAR        = 7
    ENTAO       = 8
    INICIO      = 9
    INTEGER     = 10
    ENQUANTO    = 11
    PROCEDURE   = 12
    PRINCIPAL   = 13
    REAL        = 14
    REPITA      = 15
    ATRIBUIT    = 16
    ERRO        = 17
    WS          = 18
    COMMENT     = 19 
    OPEREL      = 20
    OPERARIT2   = 21
    OPERARIT1   = 22
    TIPO        = 23
    CONST       = 24
    ENDLINE     = 25
    SENAO       = 26
    VIRGULA     = 27

class TOKEN_ATRIBUTO_OPEREL(enum.IntEnum):
    LT = 1
    LE = 2
    GT = 3
    GE = 4
    EQ = 5
    NQ = 6

class TOKEN_ATRIBUTO_OPEARIT(enum.IntEnum):
    SUM     = 1
    SUB     = 2
    TIMES   = 3
    DIV     = 4 

class TOKEN_ATRIBUTO_CONST(enum.IntEnum):
    INT = 1
    CHAR = 2
    REAL = 3
    EXP = 4