amount = int(input("Please enter the amount of money you want to withdraw:"))

hundrednote = amount//100
fifetynote = (amount%100)//50
tennote = ((amount%100)%50)//10

print("the amount of hundred rupee notes are", hundrednote)
print("the amount of fifety rupee notes are", fifetynote)
print("the amount of ten rupee notes are", tennote)