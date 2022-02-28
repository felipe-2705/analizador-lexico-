import analisador_lexico.tabTransicao as trans
import analisador_lexico.enums as enums 
import analisador_lexico.tokens as tokens
import analisador_lexico.readArq as readArq
import analisador_lexico.tabSimbolos as simb


class Lex:
    def __init__(self,arquivo,simb):
        self.__arq = readArq.Leitor(arquivo)
        self.trans = trans.tabTransicao()
        self.simb  = simb
        self.__column = 0 
        self.__line = 0 
        self.__proxChar = self.__arq.proxChar()
        self.lexema = ""

    def proxchar(self):
        self.lexema += self.__proxChar
        self.__proxChar = self.__arq.proxChar()
        self.__column += 1

    def error(self):
        print("ERROR CHARACTER INESPERADO '{0} {1}' na linha {2} coluna {3}".format(self.lexema,self.__proxChar,self.__line,self.__column) )
        exit(0)

    def processToken(self):
        state = 1
        while self.__proxChar != '' or self.lexema != "":
            state = self.trans.move(state,self.__proxChar)
            if(state == 10):
                self.proxchar()
                self.lexema = ""
                return tokens.setCOMANDBREAK(self.__line,self.__column)
            elif state == 11:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPENPARENT(self.__line,self.__column)
            elif state == 12:
                self.proxchar()
                self.lexema = ""
                return tokens.setCLOSEPARENT(self.__line,self.__column)
            elif state == 13:
                pos = self.simb.table(self.lexema,None,None)
                self.lexema = ""
                return tokens.setID(pos,self.__line,self.__column)
            elif state == 28:
                self.lexema =""
                return tokens.setSE(self.__line,self.__column)
            elif state == 32:
                self.lexema =""
                return tokens.setFIM(self.__line,self.__column)
            elif state == 37:
                self.lexema =""
                return tokens.setCHAR(self.__line,self.__column)
            elif state == 44:
                self.lexema =""
                return tokens.setENTAO(self.__line,self.__column)
            elif state == 54:
                self.lexema =""
                return tokens.setINICIO(self.__line,self.__column)
            elif state == 57:
                self.lexema =""
                return tokens.setINTEGER(self.__line,self.__column)
            elif state == 59:
                self.lexema =""
                return tokens.setENQUANTO(self.__line,self.__column)
            elif state == 63:
                self.lexema =""
                return tokens.setPROCEDURE(self.__line,self.__column)
            elif state == 66:
                self.lexema =""
                return tokens.setPRINCIPAL(self.__line,self.__column)
            elif state == 69:
                self.lexema =""
                return tokens.setREAL(self.__line,self.__column)
            elif state == 73:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEARIT1(enums.TOKEN_ATRIBUTO_OPEARIT.SUM,self.__line,self.__column)
            elif state == 74:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEARIT1(enums.TOKEN_ATRIBUTO_OPEARIT.SUB,self.__line,self.__column)
            elif state == 72:
                self.lexema =""
                return tokens.setREPITA(self.__line,self.__column)
            elif state == 76:
                self.proxchar()
                self.lexema =""
                return tokens.setATRIBUIT(self.__line,self.__column)
            elif state == 77:
                self.error()
            elif state == 78:
                self.proxchar()
                self.lexema = ""
                state = 1
            elif state == 80:
                self.proxchar()
                self.lexema = ""
                state = 1
            elif state == 82:
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.LT,self.__line,self.__column)
            elif state == 83:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.NQ,self.__line,self.__column)
            elif state == 84:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.LE,self.__line,self.__column)
            elif state == 86:
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.GT,self.__line,self.__column)
            elif state == 87:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.GE,self.__line,self.__column)
            elif state == 89:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEREL(enums.TOKEN_ATRIBUTO_OPEREL.EQ,self.__line,self.__column)
            elif state == 90:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEARIT2(enums.TOKEN_ATRIBUTO_OPEARIT.TIMES,self.__line,self.__column)
            elif state == 91:
                self.proxchar()
                self.lexema = ""
                return tokens.setOPEARIT2(enums.TOKEN_ATRIBUTO_OPEARIT.DIV,self.__line,self.__column)
            elif state == 95:
                valor = int(self.lexema)
                pos = self.simb.table(self.lexema, enums.TOKEN_ATRIBUTO_CONST.INT, valor)
                self.lexema = ""
                return tokens.setCONST(pos,self.__line,self.__column)
            elif state == 98:
                valor = float(self.lexema)
                pos = self.simb.table(self.lexema, enums.TOKEN_ATRIBUTO_CONST.REAL, valor)
                self.lexema = ""
                return tokens.setCONST(pos,self.__line,self.__column)
            elif state == 102:
                valor = float(self.lexema)
                pos = self.simb.table(self.lexema, enums.TOKEN_ATRIBUTO_CONST.EXP, valor)
                self.lexema = ""
                return tokens.setCONST(pos,self.__line,self.__column)
            elif state == 105:
                valor = self.lexema
                pos = self.simb.table(self.lexema, enums.TOKEN_ATRIBUTO_CONST.CHAR, valor)
                self.lexema = ""
                return tokens.setCONST(pos,self.__line,self.__column)
            elif state == 106:
                self.proxchar()
                self.lexema = ""
                self.__line += 1
                self.__column = 0
                state = 1
            elif state == 110:
                self.lexema = ""
                return tokens.setSENAO(self.__line,self.__column)
            elif state == 111:
                self.proxchar()
                self.__line += 1
                self.__column = 0
            elif state == 112:
                self.lexema = ""
                self.proxchar()
                return tokens.setVIRGULA(self.__line,self.__column)
            else:
                self.proxchar()
        return None

    def proxToken(self):
        return self.processToken()



