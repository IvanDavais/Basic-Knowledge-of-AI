def say_hello():
    print("你好，我是say hello!")

# name 属性可以做到，测试模块的代码只在测试情况下被运行，而在被导入是不会被执行
if __name__ == "__main__":
    print("小明开发的模板！")
    say_hello()

print("---------------------------")