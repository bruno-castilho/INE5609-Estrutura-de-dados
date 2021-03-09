

class HashMapBase:
    def __init__(self, m):
        self._m = m
        self._vetor = [-1] * self._m
    
    def _hash_function(self, s):
        return len(s) % self._m

    def __len__(self):
        return self._m

    def __getitem__(self, pos):
        return self._vetor[pos]
    
    def __setitem__(self, s):
        pos = self._hash_function(s)
        
        cont = 0
        while cont < self._m:
            if self.__getitem__(pos) == -1 or self.__getitem__(pos) == -2:
                self._vetor[pos] = s
                return

            if self._m -1 > pos:
                pos += 1

            else: 
                pos = 0
            
            cont += 1
        
        print("Table is empty")

    def __removeitem__(self, s):
        pos = self._hash_function(s)

        cont = 0
        while cont < self._m:
            if self.__getitem__(pos) == s:
                self._vetor[pos] = -2
                return

            if self._m -1 > pos:
                pos += 1

            else: 
                pos = 0
            
            cont += 1
        
        print("Item not found")

    def __show__(self):

        for cell in self._vetor:
            print(cell)
    


m = int(input())

HashMapBase = HashMapBase(m)

while  True:
    inp = int(input())

    if(inp == 0):
        HashMapBase.__setitem__(input())
        
    elif(inp == 1):
        HashMapBase.__removeitem__(input())

    elif(inp == -1):
        break
    else:
        print("Digite '1', '0' e '-1'")


HashMapBase.__show__()
    
    
