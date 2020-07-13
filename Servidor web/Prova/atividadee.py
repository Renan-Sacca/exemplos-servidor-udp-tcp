def par(N):
    if N == 0:
        print(0)
        return 0
    if N % 2 == 0:
        z = par(N-2)
        print(N)
    else:
        z = par(N-1)

par(11)