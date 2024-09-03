import math
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
lcm=abs(n1*n2)//math.gcd(n1,n2)
print(lcm)