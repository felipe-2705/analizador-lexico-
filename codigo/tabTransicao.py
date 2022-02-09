import csv

arquivo = "./data/tabela.csv"

class tabTransicao:
    def __init__(self):
        global arquivo 
        self._table = []
        self.__ler_arquivo_dados(arquivo)

    def __ler_arquivo_dados(self, arquivo):
        with open(arquivo,newline='') as csv_file:
            csv_leitor = csv.reader(csv_file,delimiter=',') 
            for row in csv_leitor:
                self._table.append(row)
    
    def imprime(self):
        for row in self._table:
            print(row)

    def __getSimbolColumn(self,c):
        try: 
            column = self._table[0].index(c)
            return column
        except ValueError:            
            return self._table[0].index('outros')

    def __preparechar(self,char):
        if(char == 'E'):
            return char
        if('0' <= char and char <= '9'):
            return 'digito'
        if(char == '\t'):
            return '\\t'
        if(char == '\n'):
            return '\\n'
        if(char.isupper()):
            return 'letra'
        return char

    def move(self,state,char):
        c = self.__preparechar(char)
        c = self.__getSimbolColumn(c)
        return self._table[state][c]




tab = tabTransicao()
tab.imprime()
print(tab.move(103,'?'))