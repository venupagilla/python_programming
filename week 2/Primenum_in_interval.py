n1=int(input("Enter the interval start : "))
n2=int(input("Enter the interval end : "))
for i in range(n1,n2+1):
    isprime=True
    for j in range(2,i):
        if i % j==0:
            isprime=False
            break
    if isprime and i!=1:
        print(i)