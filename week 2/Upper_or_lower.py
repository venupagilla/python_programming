n=input("Enter a number or letter")
if n.isdigit():
    print("Entered character is a digit")
elif n.islower():
    print("Entered character is a lower letter")
else:
    print("Entered character is a Upper letter")