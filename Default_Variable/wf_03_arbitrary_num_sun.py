def arbitrary_num_sun(*args):
    num = 0
    print(args)
    for n in args:
        num += n
    print(num)


arbitrary_num_sun(1, 2, 6, 100, 1220)
