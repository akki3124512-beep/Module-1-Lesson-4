# This calculates the square root of your number
y = input("Enter the number you want to find the square root of:")

# If you do not convert to an integer, it will give you an error because you cannot do math on a string.
# To find the square root of a number, you use the exponential command ** with 0.5 as the exponent.
x = int(y)**0.5

# Finally, we print the result.
print("The square root of", y, "is", x)