from CircularLinkedList import CircularLinkedList

def josephus(n,m):
    my_list = CircularLinkedList()

    while n >= 1 :
        my_list.push(n)
        n -= 1


    pivot = my_list._tail

    while len(my_list) > 1:
        number = 1
        if len(my_list) > m:
            while number <= m:
                pivot = pivot._next
                number += 1
        else:
            pivot = pivot._next

        my_list._remove(pivot)
        


    

    
    return my_list._tail._element
    


cases = int(input())
values = []

while cases > 0:
    n = int(input())
    m = int(input())
    values.append([n,m])
    cases -= 1


for value in values:
    n = value[0]
    m = value[1]
    result = josephus(n,m)

    print(f'Usando n={n}, m={m}, resultado={result}')

