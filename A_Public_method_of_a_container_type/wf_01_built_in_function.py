
"""Notice: del can be uesd to be method or function"""
a= [1,2,3]

del a[1]
print(a)

del(a[0])
print(a)

"""max and min function in list, string, tuple, dictionary"""
t_str = "dasfjkhfkjghnmziojqw"
print(max(t_str))
n_str = "9182"
print(max(n_str))

n_list = [2, 4, 5, 19]
print(max(n_list))
print(min(n_list))

char_dictionary ={"a":"x",
                  "b":"y",
                  "c":"z"}
print(max(char_dictionary))
print(min(char_dictionary))

t_tuple = ("a", "b", "z")
print(max(t_str))
print(min(t_tuple))

"""Compare the size"""
str1 = "aaa"
str2 = "bbb"
print(str1>str2)
print(str1<str2)

char_list1 = ["a", "b", "c"]
char_list2 =["x", "y", "z"]
print(char_list1<char_list2)

char_tuple1 = (1, 1, 1)
char_tuple2 = (2, 2, 2)
print(char_tuple1>char_tuple2)

# notice: direction cannot be compared

