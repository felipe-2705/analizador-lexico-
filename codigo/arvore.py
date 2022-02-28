class No:
    def __init__(self,value):
        self.value = value 
        self.filhos = []
    def add_filho(self,no):
        self.filhos.append(no)
    def print_subarvores(self,):
        print(self.value)
        for no in self.filhos:
            no.print_subarvores()
