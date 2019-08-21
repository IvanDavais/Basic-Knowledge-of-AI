info_tuple = ("ZhangSan", 19, 18.2, "ZhangSan")

"""index's usage in touple"""
print(info_tuple[1])
print(info_tuple.index("ZhangSan"))

"""count's usage in touple"""
print(info_tuple.count("ZhangSan"))
print(len(info_tuple))

"""iteration for tuple"""
for info in info_tuple:
    print(info)

"""tuple convert to list"""
info_list = list(info_tuple)
print(type(info_list))
print(info_list)


"""list convert to touple"""
name_list = ["zhangsan", "lisi", "wangwu"]
name_touple = tuple(name_list)
print(type(name_touple))
print(name_touple)