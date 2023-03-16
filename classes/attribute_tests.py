class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
x = A()
print(x.pub)

x.pub = x.pub + " and my value can be changed"
print(x.pub)

print(x._prot)
