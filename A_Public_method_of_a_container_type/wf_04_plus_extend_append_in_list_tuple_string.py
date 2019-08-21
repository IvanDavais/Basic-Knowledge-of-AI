""" '+' in list"""
num_list1 = [1, 2]
num_list2 = [3, 5]
print(num_list1+num_list2)


""" '+' in tuple"""
num_tuple1 = (1, 3)
num_tuple2 = (2, 5)
print(num_tuple1+num_tuple2)


""" '+' in string """
hello_string = "hello "
world_string = "world"
print(hello_string+world_string)


"""The difference between extend & append"""
# extend
t_list =[1, 2, 3, 4]
t_list.extend([5, 6])
# t_list.extend(5) Notice: extend can not plus single number except for a list of number
print(t_list)

#append: situation A
t_list.append(7)
print(t_list)

#append: situation B
t_list.append([8, 9])
print(t_list)