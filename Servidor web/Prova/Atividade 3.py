
a=65
b=15
m=0
while (True):
    if (a>b):
        b,a=a,b
    m+=b;
    if m%a == 0 and m%b==0:
        print(m)
        break
