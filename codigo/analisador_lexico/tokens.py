from analisador_lexico.enums import TOKEN_TIPO


class TOKEN:
    def __init__(self,tipo,atributo,linha,coluna):
        self.tipo = tipo
        self.atributo = atributo
        self.linha = linha
        self.coluna = coluna


def setCOMANDBREAK(linha,coluna):
    return TOKEN(TOKEN_TIPO.COMANDBREAK,None,linha,coluna)

def setOPENPARENT(linha,coluna):
    return TOKEN(TOKEN_TIPO.OPENPARENT,None,linha,coluna)

def setCLOSEPARENT(linha,coluna):
    return TOKEN(TOKEN_TIPO.CLOSEPARENT,None,linha,coluna)

def setID(atributo,linha,coluna):
    return TOKEN(TOKEN_TIPO.ID,atributo,linha,coluna)

def setSE(linha,coluna):
    return TOKEN(TOKEN_TIPO.SE,None,linha,coluna)

def setFIM(linha,coluna):
    return TOKEN(TOKEN_TIPO.FIM,None,linha,coluna)

def setCHAR(linha,coluna):
    return TOKEN(TOKEN_TIPO.CHAR,None,linha,coluna)

def setENTAO(linha,coluna):
    return TOKEN(TOKEN_TIPO.ENTAO,None,linha,coluna)

def setSENAO(linha,coluna):
    return TOKEN(TOKEN_TIPO.SENAO,None,linha,coluna)

def setINICIO(linha,coluna):
    return TOKEN(TOKEN_TIPO.INICIO,None,linha,coluna)

def setENQUANTO(linha,coluna):
    return TOKEN(TOKEN_TIPO.ENQUANTO,None,linha,coluna)

def setPROCEDURE(linha,coluna):
    return TOKEN(TOKEN_TIPO.PROCEDURE,None,linha,coluna)

def setPRINCIPAL(linha,coluna):
    return TOKEN(TOKEN_TIPO.PRINCIPAL,None,linha,coluna)

def setREAL(linha,coluna):
    return TOKEN(TOKEN_TIPO.REAL,None,linha,coluna)

def setREPITA(linha,coluna):
    return TOKEN(TOKEN_TIPO.REPITA,None,linha,coluna)

def setATRIBUIT(linha,coluna):
    return TOKEN(TOKEN_TIPO.ATRIBUIT,None,linha,coluna)

def setOPEREL(atributo,linha,coluna):
    return TOKEN(TOKEN_TIPO.OPEREL,atributo,linha,coluna)

def setOPEARIT1(atributo,linha,coluna):
    return TOKEN(TOKEN_TIPO.OPERARIT1,atributo,linha,coluna)

def setOPEARIT2(atributo,linha,coluna):
    return TOKEN(TOKEN_TIPO.OPERARIT2,atributo,linha,coluna)

def setCONST(atributo,linha,coluna):
    return TOKEN(TOKEN_TIPO.CONST,atributo,linha,coluna)

def setINTEGER(linha,coluna):
    return TOKEN(TOKEN_TIPO.INTEGER,None,linha,coluna)

def setVIRGULA(linha,coluna):
    return TOKEN(TOKEN_TIPO.VIRGULA,None,linha,coluna)
