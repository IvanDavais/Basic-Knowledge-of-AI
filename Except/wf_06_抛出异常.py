def input_password():
    passwd = input("请输入你的密码: ")
    if len(passwd) >= 8:
        return "你的密码为: %s "% passwd
    else:
        ex = Exception("您好，你输入的密码长度不够8位，请重新输入！ ")
        raise ex


try:
    print(input_password())
except Exception as result:
    print("出现异常: %s" % result)