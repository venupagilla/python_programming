letter=input("Enter the sentence you want to capitalize : ")
new_letter=""
for i in range(len(letter)):
    if letter[i-1] == " " or i==0:
        new_letter+=letter[i].upper()
    else:
        new_letter+=letter[i]
print(new_letter)