import csv
import re

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
        for i in range(1,len(self._table[0])):
            regx = self._table[0][i]
            if re.match(regx,c):
                return i

    def move(self,state,char):
       ## c = self.__preparechar(char)
        c = self.__getSimbolColumn(char)
        return int(self._table[state][c])
 