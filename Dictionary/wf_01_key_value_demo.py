Fan_Wan = {"name": "wanfan",
           "age": 27,
           "height": 172,
           "weight": 72}

print(Fan_Wan)


"""Search in dictionary"""
print(Fan_Wan["age"])


"""Add in dictionary"""
Fan_Wan["Gender"] = True
print(Fan_Wan)


"""Modify in dictionary"""
Fan_Wan["name"] = "Jasmine"
print(Fan_Wan)


"""Delete in dictionary"""
Fan_Wan.pop("Gender")
print(Fan_Wan)


"""len in dictionary"""
print(len(Fan_Wan))

"""update in dictionary"""
temp_dictionary = {"favorite_music": "pop"}
Fan_Wan.update(temp_dictionary)
print(Fan_Wan)

# notice: when you use update method and there are some repetitive items,
# the new items will replace the old items.
another_dictionary = {"name": "Coco"}
Fan_Wan.update(another_dictionary)
print(Fan_Wan)


"""clear in dictionary """
Fan_Wan.clear()
print(Fan_Wan)