"""Notice: this program is for illustrate how to use multi-inherit
and when exit some same method in different parent class, which the method
of the child class will invoke.

** Use className.__MRO__ could identify the order of methods invoked.
"""
class A:
    def demo(self):
        print("A demo")

    def test(self):
        print("A test")


class B:
    def demo(self):
        print("B demo")

    def test(self):
        print("B test")

class C(A, B):
    pass


c = C()
c.demo()
c.test()
print(C.__mro__)