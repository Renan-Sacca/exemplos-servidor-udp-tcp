def ha(n):
    print(n)
    if n==1:
        return 1
    if n%2 == 0:
        return ha(n/2)
    else:
        return ha((n*3) + 1)

print(ha(3))