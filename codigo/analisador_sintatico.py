import analisador_lexico.analizadorLexico as lex 
import analisador_lexico.tabSimbolos as simb 
import analisador_lexico.enums as enum 
import analisador_lexico.tokens as tk 
import arvore 

first_declaracao_variavel =  [ 
    enum.TOKEN_TIPO.CHAR,
    enum.TOKEN_TIPO.INTEGER,
    enum.TOKEN_TIPO.REAL
]

first_comando = [
    enum.TOKEN_TIPO.SE,
    enum.TOKEN_TIPO.ENQUANTO,
    enum.TOKEN_TIPO.REPITA,
    enum.TOKEN_TIPO.ID
]

first_selecao = [
    enum.TOKEN_TIPO.SE
]

first_repeticao = [
    enum.TOKEN_TIPO.ENQUANTO,
    enum.TOKEN_TIPO.REPITA
]

first_atribuicao = [
    enum.TOKEN_TIPO.ID
]

first_OPERACAO = [
    enum.TOKEN_TIPO.OPENPARENT,
    enum.TOKEN_TIPO.ID,
    enum.TOKEN_TIPO.CONST
]

first_EXPRESSAO1 = [
    enum.TOKEN_TIPO.OPEREL
]

first_TERMO = [
    enum.TOKEN_TIPO.OPENPARENT,
    enum.TOKEN_TIPO.ID,
    enum.TOKEN_TIPO.CONST
]

class Sintax:
    def __init__ (self, arq):
        self.__simb =  simb.SimbolTable()
        self.__lex = lex.Lex(arq,self.__simb) 
        self.proxToken = self.__lex.proxToken()

    def nextToken(self):
        return self.__lex.proxToken()

    def error(self,esp):
        print("ERRO: token inesperado.  Esperado {0} na linha {1} coluna {2}",esp,self.proxToken.linha,self.proxToken.coluna)
        exit(0)

    def start(self):
        self.arvore = self.__proc_S()

    def __proc_S(self):
        no = arvore.No('S')
        if self.proxToken == None:
            return no 
        if self.proxToken.tipo == enum.TOKEN_TIPO.PROCEDURE: 
            no.add_filho(arvore.No("procedure"))
            self.proxToken = self.nextToken()
            if self.proxToken.tipo == enum.TOKEN_TIPO.PRINCIPAL:
                no.add_filho(arvore.No("principal"))
                self.proxToken = self.nextToken()
                filho =  self.__proc_BLOCO()
                no.add_filho(filho)
            else:
                self.error('principal')
        else:
            self.error('procedure')
        return no 

    def __proc_BLOCO(self):
        no = arvore.No('BLOCO')
        if self.proxToken == None:
            return no 
        if self.proxToken.tipo == enum.TOKEN_TIPO.INICIO:
            no.add_filho(arvore.No('inicio'))
            self.proxToken = self.nextToken()
            no.add_filho(self.__proc_DECLARACOES_VARIAVEIS())
            no.add_filho(self.__proc_COMANDOS())
            if self.proxToken.tipo == enum.TOKEN_TIPO.FIM:
                no.add_filho(arvore.No('fim'))
                self.proxToken = self.nextToken()
            else:
                self.error('fim')
        else: 
            self.error('inicio')
        return no 
    
    def __proc_DECLARACOES_VARIAVEIS(self):
        global first_declaracao_variavel
        no = arvore.No('DECLARACOES-VARIAVEIS')
        while self.proxToken.tipo in first_declaracao_variavel:
            no.add_filho(self.__proc_DECLARACAO_VARIAVEL())
        return no 

    def __proc_DECLARACAO_VARIAVEL(self):
        global first_declaracao_variavel
        no = arvore.No('DECLARACAO-VARIAVEL')
        if self.proxToken == None:
            return no 
        no.add_filho(self.__proc_TIPO())
        no.add_filho(self.__proc_LISTA_IDS())
        if self.proxToken.tipo == enum.TOKEN_TIPO.COMANDBREAK:
            no.add_filho(arvore.No(';'))
            self.proxToken = self.nextToken()
        else: 
            self.error(';')
        return no 

    def __proc_LISTA_IDS(self):
        no = arvore.No('LISTA-IDS')
        if self.proxToken == None:
            return no 
        if self.proxToken.tipo  == enum.TOKEN_TIPO.ID:
            no.add_filho(arvore.No('id'))
            self.proxToken = self.nextToken()
            no.add_filho(self.__proc_LISTA_IDS1())
        else:
            self.error('id')
        return no 
    
    def __proc_LISTA_IDS1(self):
        no = arvore.No('LISTA-IDS\'')
        if self.proxToken.tipo == enum.TOKEN_TIPO.VIRGULA:
            no.add_filho(arvore.No(','))
            self.proxToken = self.nextToken()
            no.add_filho(self.__proc_LISTA_IDS())
        return no 
    
    def __proc_TIPO(self):
        no = arvore.No('TIPO')
        if self.proxToken.tipo == enum.TOKEN_TIPO.INTEGER:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No('integer'))
        elif self.proxToken.tipo == enum.TOKEN_TIPO.CHAR:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No('char'))
        elif self.proxToken.tipo == enum.TOKEN_TIPO.REAL:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No('real'))
        else: 
            self.error('integer, char ou real')
        return no 
    
    def __proc_COMANDOS(self):
        global first_comando
        no = arvore.No("COMANDOS")
        while self.proxToken.tipo in first_comando:
            no.add_filho(self.__proc_COMANDO())
        return no

    def __proc_COMANDO(self):
        global first_atribuicao
        global first_repeticao
        global first_selecao

        no = arvore.No("COMANDO")
        if self.proxToken.tipo in first_selecao:
            no.add_filho(self.__proc_SELECAO())
        elif self.proxToken.tipo in first_atribuicao:
            no.add_filho(self.__proc_ATRIBUICAO())
        elif self.proxToken.tipo in first_repeticao:
            no.add_filho(self.__proc_REPETICAO())
        else:
            self.error('se, enquanto, repita ou id')    
        return no
    
    def __proc_SELECAO(self):
        no = arvore.No("SELECAO")
        if self.proxToken.tipo == enum.TOKEN_TIPO.SE:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("se"))
            if self.proxToken.tipo == enum.TOKEN_TIPO.OPENPARENT:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No("("))
                no.add_filho(self.__proc_EXPRESSAO())
                if self.proxToken.tipo == enum.TOKEN_TIPO.CLOSEPARENT:
                    self.proxToken = self.nextToken()
                    no.add_filho(arvore.No(")"))
                    if self.proxToken.tipo == enum.TOKEN_TIPO.ENTAO:
                        self.proxToken = self.nextToken()
                        no.add_filho(self.__proc_BLOCO())
                        no.add_filho(self.__proc_S1())
                    else:
                        self.error("entao")
                else: 
                    self.error(")")
            else:
                self.error("(")
        else:
            self.error("se")
        return no
    
    def __proc_S1(self):
        no = arvore.No("S\'")
        if self.proxToken.tipo == enum.TOKEN_TIPO.SENAO:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("senao"))
            no.add_filho(self.__proc_BLOCO())
        return no 
    
    def __proc_REPETICAO(self):
        no = arvore.No("REPETICAO")
        if self.proxToken.tipo == enum.TOKEN_TIPO.ENQUANTO:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("enquanto"))
            if self.proxToken.tipo == enum.TOKEN_TIPO.OPENPARENT:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No("("))
                no.add_filho(self.__proc_EXPRESSAO())
                if self.proxToken.tipo == enum.TOKEN_TIPO.CLOSEPARENT:
                    self.proxToken = self.nextToken()
                    no.add_filho(arvore.No(")"))
                    no.add_filho(self.__proc_BLOCO())
                else:
                    self.error(')')
            else:
                self.error('(')
        elif self.proxToken.tipo == enum.TOKEN_TIPO.REPITA:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("repita"))
            no.add_filho(self.__proc_BLOCO())
            if self.proxToken.tipo == enum.TOKEN_TIPO.ENQUANTO:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No("enquanto"))
                if self.proxToken.tipo == enum.TOKEN_TIPO.OPENPARENT:
                    self.proxToken = self.nextToken()
                    no.add_filho(arvore.No("("))
                    no.add_filho(self.__proc_EXPRESSAO())
                    if self.proxToken.tipo == enum.TOKEN_TIPO.CLOSEPARENT:
                        self.proxToken = self.nextToken()
                        no.add_filho(arvore.No(")"))
                        if self.proxToken.tipo == enum.TOKEN_TIPO.COMANDBREAK:
                            self.proxToken = self.nextToken()
                            no.add_filho(arvore.No(";"))
                        else:
                            self.error(';')
                    else:
                        self.error(')')
                else:
                    self.error('(')
            else:
                self.error("enquanto")
        else:
            self.error("enquanto ou repita")
        return no 

    def __proc_ATRIBUICAO(self):
        no = arvore.No("ATRIBUICAO")
        if self.proxToken.tipo == enum.TOKEN_TIPO.ID:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("id"))
            if self.proxToken.tipo == enum.TOKEN_TIPO.ATRIBUIT:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No(":="))
                no.add_filho(self.__proc_EXPRESSAO())
                if self.proxToken.tipo == enum.TOKEN_TIPO.COMANDBREAK:
                    self.proxToken = self.nextToken()
                    no.add_filho(arvore.No(";"))
                else:
                    self.error(";")
            else:
                self.error(":=")
        else:
            self.error("id")
        return no 

    def __proc_EXPRESSAO(self):
        global first_OPERACAO
        no = arvore.No("EXPRESSAO")
        if self.proxToken.tipo in first_OPERACAO:
            no.add_filho(self.__proc_OPERACAO())
            no.add_filho(self.__proc_EXPRESSAO1()) 
        else:
            self.error("(, id, const-char ou num")
        return no 
    
    def __proc_EXPRESSAO1(self):
        global first_EXPRESSAO1
        no= arvore.No("EXPRESSAO\'")
        while self.proxToken.tipo in first_EXPRESSAO1:
            no.add_filho(self.__proc_OPREL())
            no.add_filho(self.__proc_OPERACAO())
        return no

    def __proc_OPREL(self):
        no = arvore.No("OPREL")
        if self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.EQ:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("=="))
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.NQ:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("<>"))
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.LT:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("<"))
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.GT:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No(">"))
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.LE:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("<="))
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEREL.GE:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No(">="))
        else:
            self.error("== , <>, <= ,>= ,< ou >")
        return no
    
    def __proc_OPERACAO(self):
        global first_TERMO
        no = arvore.No("OPERACAO")
        if self.proxToken.tipo in first_TERMO:
            no.add_filho(self.__proc_TERMO())
            no.add_filho(self.__proc_OPERACAO1())
        else:
            self.error("(, id, const-char ou num")
        return no 
    
    def __proc_OPERACAO1(self):
        no = arvore.No("OPERACAO1")
        while self.proxToken.tipo == enum.TOKEN_TIPO.OPERARIT1:
            no.add_filho(self.__proc_OPEARIT1())
            no.add_filho(self.__proc_TERMO())
        return no 

    def __proc_TERMO(self):
        no = arvore.No("TERMO")
        no.add_filho(self.__proc_FATOR())
        no.add_filho(self.__proc_TERMO1())
        return no 
    
    def __proc_TERMO1(self):
        no = arvore.No("TERMO1")
        while self.proxToken.tipo == enum.TOKEN_TIPO.OPERARIT2:
            no.add_filho(self.__proc_OPEARIT2())
            no.add_filho(self.__proc_FATOR())
        return no
        
    def __proc_FATOR(self):
        no = arvore.No("FATOR")
        if self.proxToken.tipo == enum.TOKEN_TIPO.OPENPARENT:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("("))
            no.add_filho(self.__proc_EXPRESSAO())
            if self.proxToken.tipo == enum.TOKEN_TIPO.CLOSEPARENT:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No(")"))
            else:
                self.error(")")
        elif self.proxToken.tipo == enum.TOKEN_TIPO.ID:
            self.proxToken = self.nextToken()
            no.add_filho(arvore.No("id"))
        elif self.proxToken.tipo == enum.TOKEN_TIPO.CONST:
            no.add_filho(self.__proc_CONSTANTE())
        else:
            self.error("(, id ou constante")
        return no

    def __proc_OPEARIT1(self):
        if self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEARIT.SUM:
            self.proxToken = self.nextToken()
            no = arvore.No("+")
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEARIT.SUB:
            self.proxToken = self.nextToken()
            no = arvore.No("-")            
        return no

    def __proc_OPEARIT2(self):
        if self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEARIT.TIMES:
            self.proxToken = self.nextToken()
            no = arvore.No("*")
        elif self.proxToken.atributo == enum.TOKEN_ATRIBUTO_OPEARIT.DIV:
            self.proxToken = self.nextToken()
            no = arvore.No("/")            
        return no
    
    def __proc_CONSTANTE(self):
        no = arvore.No("CONSTANTE")
        if self.proxToken.tipo == enum.TOKEN_TIPO.CONST:
            if self.proxToken.atributo == enum.TOKEN_ATRIBUTO_CONST.CHAR:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No("const-char"))
            else:
                self.proxToken = self.nextToken()
                no.add_filho(arvore.No("const-num"))
        else:
            self.error("constante")

        return no 



a = Sintax("teste.txt")
a.start()
a.arvore.print_subarvores()
