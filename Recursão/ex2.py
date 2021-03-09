def caracteres(string):
        try:
            arr = list(string)

            print(arr[-1])

            arr.pop(-1)
            string = ''.join(arr)
            
            return caracteres(string)

        except:
            return


caracteres(input())