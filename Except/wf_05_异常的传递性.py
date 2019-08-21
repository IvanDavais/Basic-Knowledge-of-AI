# 利用异常的传递性，在主程序捕获异常

def cul1():
    num = int(input("请输入正整数："))

def cul2():
    cul1()

try:
    cul2()
except Exception as result:
    print("出现异常： %s " %result)
    