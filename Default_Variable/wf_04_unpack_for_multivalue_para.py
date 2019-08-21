def unpack(*args, **kwargs):
    print(args)
    print(kwargs)


num_tuple = (1, 3, 6, 10)
name_dic = {"name": "wanfan",
            "age": 27,
            "gender": "male"}

unpack(*num_tuple, **name_dic)

