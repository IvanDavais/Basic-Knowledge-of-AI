hello_str = "hello world"

"""startswith()"""
print(hello_str.startswith("h"))


"""endswith()"""
print(hello_str.endswith("world"))


"""find() Notice: if you use find method and index method, there are some differences,
if the item you want to find is not exited, index method will occur error,
however, the find method will not and display -1 which means this item 
didn't be contained in this string."""

print(hello_str.find("llo"))

"""replace()  Notice: the replace method will not change contend of original method"""
print(hello_str.replace("world","python"))
print(hello_str)
