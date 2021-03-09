def crescente(list):
        try:
            if(list[0] >= list[1]):
                return False
            else:
                list.pop(0)
                return crescente(list)
            
        except:
            return True

lista = []



try: 
    while True:
        lista.append(int(input()))
except:
    pass
        

        


print(crescente(lista))