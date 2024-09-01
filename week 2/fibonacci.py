n=int(input("Enter the number of elements you want fibonacci series for : "))
start=0
update=1
while n>0:
    print(start)
    start,update=update,update+start
    n=n-1

