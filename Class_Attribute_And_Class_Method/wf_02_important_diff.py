class Tool(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count += 1


tool1 = Tool("锄头")
tool2 = Tool("棒子")

tool1.count = 99
print(tool1.count)

print(Tool.count)