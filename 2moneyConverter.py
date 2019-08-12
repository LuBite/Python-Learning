# --------美元人民币转换--------
# --------PROGRAM : Dollar To TMB --------
# Dollar currency rate is 7.0637, ￥ = $ * 7.0637
# EXP : Enter $5, $5 equals ￥35.3185
# DATE : 2019.8.12

# Ask the user to input $ and assign it to the $ variable
dollar = input("Please enter dollars: ")

# Convert from string to integer
dollar = int(dollar)

# Perform calculation by multiplying 7.0637 times $
CNY = dollar * 7.0637

# Print results using format()
print("{} dollars equals {} Yuan".format(dollar, CNY))
