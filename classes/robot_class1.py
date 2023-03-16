class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year
    def say_hi(self):
        if self.name:
            print("Hi, i am " + self.name)
        else:
            print("Hi, i am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when i was created!")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_build_year(self, build_year):
        self.build_year = build_year
    def get_build_year(build_year):
        return set.build_year
x = Robot("Henry", 2008)
y = Robot()
x.set_name("Colloso")
y.set_name("Marvin")
x.say_hi()
y.say_hi()

