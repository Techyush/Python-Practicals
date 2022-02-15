class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} singing {}".format(self.name, song)

    def dance(self, dance):
        return "{} is now dancing in {} style".format(self.name,dance)


blu = Parrot("Blu", 10)

print(blu.sing("a Good Song"))
print(blu.dance("HipHop"))
