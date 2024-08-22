def calc(princ,interest,time):
    rate=interest/100

    return princ*(1+rate)**time

principal=100000
interest=12
time=3
print(f"compund interest is {calc(principal,interest,time)}")
