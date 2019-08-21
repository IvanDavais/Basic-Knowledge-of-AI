"""string.isspace"""
space_str=" \n\t\r"
print(space_str.isspace())
print("",end="\n")


"""Does the string contain only Numbers?"""
num_str = "1"
print(num_str)
print(num_str.isnumeric())
print(num_str.isdecimal())
print(num_str.isdigit())
print("", end="\n")

# 1. those methods can't even judge decimals
num_str = "1.2"
print(num_str)
print(num_str.isnumeric())
print(num_str.isdecimal())
print(num_str.isdigit())
print("", end="\n")

# 2. string.isnumeric is most power method,
# cause it can judge Chinese number and some mathematical symbols.

num_str = "\u00b2"
print(num_str)
print(num_str.isnumeric())
print(num_str.isdecimal())
print(num_str.isdigit())
