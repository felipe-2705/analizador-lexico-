class _SimbolTableRow: 
    def __init__(self,lexema,tipo,valor):
        self._lexema = lexema
        self._tipo   = tipo 
        self._valor  = valor 

    def getRow(self):
        return [self._lexema,self._tipo,self._valor]

    def getLexema(self):
        return self._lexema

    def getTipo(self):
        return self._tipo

    def getValor(self):
        return self._valor

    def setValor(self,newvalor):
        self._valor = newvalor 
        return True
    def setTipo(self,newtipo):
        self._tipo = newtipo 
        return True

class SimbolTable:
    def __init__(self):
        self.__lastIndex = 0
        self.__table = []
    
    def table(self,newlexema,tipo,valor):
        if self.__table:
            f = [row for row in self.__table if row._lexema == newlexema]
            if f:
                try:
                    return self.__table.index(f[0])
                except ValueError:
                    print("ERRRO INESPERADO ...., VALOR NÃO ENCONTRADO %s NA TABELA DE SIMBOLOS!!!",newlexema)
                    exit()
        s = _SimbolTableRow(newlexema,tipo,valor)
        self.__table.append(s)   
        self.__lastIndex += 1
        return self.__lastIndex - 1

    def insertTipo(self,tipo,index):
        try:
            row = self.__table[index]
            row._tipo = tipo 
        except IndexError:
            print("ERRO... tentativa de mudadr tipo de um linha que nao existe na tabela... %d não encontraod ", index)
            exit()

    def insertValor(self,value, index):
        try:
            row = self.__table[index]
            row._valor = value 
        except IndexError:
            print("ERROR ... tentatia de mudanca de valor para um index %d nao encontrado ... ", index)
            exit()

    def getValor(self,index):
        try:
            row = self.__table[index]
            return row._valor
        except IndexError:
            print("ERROR ... tentativa de buscar de valor para um index %d nao encontrado ... ", index)
            exit()
    
    def getTipo(self,index):
        try:
            row = self.__table[index]
            return row._tipo 
        except IndexError:
            print("ERROR ... tentatia de buscar tipo para um index %d nao encontrado ... ", index)
            exit()
    
    def getLexema(self,index):
        try:
            row = self.__table[index]
            return row._lexema
        except IndexError:
            print("ERROR ... tentatia de buscar lexema para um index %d nao encontrado ... ", index)
            exit()
    
    def getRow(self,index):
        try:
            row = self.__table[index]
            return row 
        except IndexError:
            print("Error ... tentativa de acessar linha %d nao existente ... ", index)
            exit()
