try:
    number = int(input("请输入一个正整数："))
    result = 8 / number
except ZeroDivisionError:
    print("请输入非0整数")
except ValueError:
    print("请输入一个数字")
