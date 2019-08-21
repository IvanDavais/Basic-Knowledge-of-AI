def multivalue_parameter(num,*tuple,**dictionary):

    print(num)
    print(tuple)
    print(dictionary)


multivalue_parameter(1, "2", 3, "4", 5, name="Ivan", age=10)

num = 1
num_tuple = (2, 4, 6, 8)
name_dic = {"name": "wanfan",
            "age": 18}
multivalue_parameter(num,*num_tuple,**name_dicz)
