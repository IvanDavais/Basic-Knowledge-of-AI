try:
    number = int(input("请输入一个正整数："))
    result = 8 / number
except ZeroDivisionError:
    print("请输入非0整数")
except Exception as result:
    print("未知错误：%s " %result)
