def recursion_sum(num):

    if num == 1:
        return 1

    temp = recursion_sum(num-1)

    return temp+num

# recursion_sum(2)
print(recursion_sum(100))