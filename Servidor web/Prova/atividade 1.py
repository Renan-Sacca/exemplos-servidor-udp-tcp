def par(N):
    if N == 0:
        return 0
    if N % 2 == 0:
        return par(N-2)
    if N % 2 != 0:
        return par(N-1)


print(par(11))