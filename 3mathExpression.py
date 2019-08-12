# --------两数字加减乘除运算--------
# -------- PROGRAM : MATH ON 2 VALUES --------
# EXP : input : 5 4
#       output:
#           5 + 4 = 9
#           5 - 4 = 1
#           5 * 4 = 20
#           5 / 4 = 1.25
#           5 % 4 = 1

# Ask the user to input 2 values and store them in variables num1 num2
# split()  splits input using whitespace
num1, num2 = input("Please enter 2 numbers: ").split()

# Convert the string into regular numbers integer
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract the values entered and store in difference
difference = num1 - num2

# Multiply the values entered and store in product
product = num1 * num2

# Divide the values entered and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print the results
# format()  loads the variable values in order into the {} placeholders
print("{0} + {1} = {2}\n{0} - {1} = {3}\n{0} * {1} = {4}\n{0} / {1} = {5}\n{0} % {1} = {6}\n"
      .format(num1, num2, sum, difference, product, quotient, remainder))

