class Tool(object):

    count = 0

    @classmethod
    def show_tool(cls):
        print("Tool count: %d" %cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("锄头")
tool2 = Tool("榔头")

tool1.show_tool()