class Leitor:
    def __init__(self,nomeArquivo):
        self._bufferSize = 50  ### bytes
        self._arq = open(nomeArquivo,'r')
        self._buffer1    = self._arq.read(self._bufferSize)
        self._buffer2    = self._arq.read(self._bufferSize)
        self._prox = 0
        self._bBuffer = True ### significa que estou no primeiro buffer 
    def proxChar(self):
            if(self._bBuffer and self._buffer1):
                ### primeiro buffer
                if self._prox < len(self._buffer1):
                    prox = self._buffer1[self._prox]
                    self._prox += 1
                    return prox
                else:
                    self._prox = 0
                    self._bBuffer = False
                    self._buffer1 = self._arq.read(self._bufferSize)
                    if self._buffer2:
                        prox = self._buffer2[self._prox]
                        self._prox += 1
                    else:
                        self._arq.close()
                        return ''
                    return prox
            elif (not self._bBuffer) and self._buffer2:
                ### segundo buffer 
                if self._prox < len(self._buffer2):
                    prox = self._buffer2[self._prox]
                    self._prox += 1
                    return prox 
                else:
                    self._prox = 0
                    self._bBuffer = True
                    self._buffer2 = self._arq.read(self._bufferSize)
                    if self._buffer1:
                        prox = self._buffer1[self._prox]
                        self._prox += 1
                    else: 
                        self._arq.close()
                        return ''
                    return prox
            self._arq.close()
            return ''

