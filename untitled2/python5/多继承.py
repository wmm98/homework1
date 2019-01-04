class Base(object):
    def base(self):
        print("-----base-----")


class A(Base):
    def test(self):
        print("----test----")


class B(Base):
    def test1(self):
        print("-----test1-----")


class C(Base):
    def test2(self):
        print("-----test2-----")


class D(A, B, C):
    def test3(self):
        print("----test3----")

d = D()
d.base()
d.test()
d.test1()
d.test2()
d.test3()



