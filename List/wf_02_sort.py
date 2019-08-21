name_list = ["Ivan", "Andy", "Coco"]
number_list = [10, 8, 9, 3, 5, 2]


def name_list_sort():
    name_list.sort()
    return name_list


def number_list_sort():
    number_list.sort()
    return number_list


name_list = name_list_sort()


number_list = number_list_sort()


print(name_list)

print(number_list)

