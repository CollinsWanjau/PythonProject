class Q:
    def __init__(self, x):
        self.x = x
p1 = Q(42)
p2 = Q(4711)
print(p1.x)
p1.x = 47
p1.x = p1.x + p2.x
print(p1.x)
