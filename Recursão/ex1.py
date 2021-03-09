def nCaracteres(string):
        try:
            arr = list(string)
            arr.pop(0)

            string = ''.join(arr)
        
            return 1 + nCaracteres(string)

        except:
            return 0


print(nCaracteres(input()))

