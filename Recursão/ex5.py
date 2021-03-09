def somaRecursiva(n):
    if n <= 1:
        return 1
    else:
        return n + somaRecursiva(n - 1)


print(somaRecursiva(int(input())))
