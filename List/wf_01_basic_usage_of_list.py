name_list = ["Ivan","Andy","Coco"]

"""search index or value in name list. """
# 1.list.index[]
print(name_list.index("Andy"))
# 2.list[]
print(name_list[2])


"""Modify the value in name list."""
# 1. list[index] = **;
name_list[2] = "Eric"
print(name_list[2])


"""Add items to list."""
# 1.insert
name_list.insert(0,"jasmine")
print(name_list)
# 2.append
name_list.append("Bran")
print(name_list)
# 3.extend
temp_list = ["Bob","Cara","Marry"]
name_list.extend(temp_list)
print(name_list)


"""Delete item in list. """
# 1.remove
name_list.remove("Marry")
print(name_list)
# 2.pop
name_list.pop()
print(name_list)
# 3.pop(index)
name_list.pop(3)
print(name_list)
# 4.clear
print(name_list)
# 5.del. System don't recommend use del, cause del will delete item in internal storage.
del name_list[1]
print(name_list)


"""The usage of len"""
list_len = len(name_list)
print(list_len)


"""The usage of count"""
name_list.append("Andy")
print(name_list)
count = name_list.count("Andy")
print(count)

# notice: remove will delete the first Andy.
name_list.remove("Andy")
print(name_list)


"""The usage of sort"""
print(name_list)


def list_sort():
    number_list = [2, 9, 10, 1, 3]
    number_list.sort()
    return number_list


def name_list_sort():
    name_list.sort()
    return name_list


print(list_sort())
print(name_list_sort())






