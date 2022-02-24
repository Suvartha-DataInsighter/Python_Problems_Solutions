class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def information(self):
        print("If iam a cat.My name is{}.Iam {} years old.".format(self.name,self.age))
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def information(self):
        print("If iam a Dog.My name is {},{}years old".format(self.name,self.age))
    def make_sound(self):
        print("Bark")
c=cat("Kitty",2.5)
d=Dog("Puppy",4)
c.information()
c.make_sound()
d.information()
d.make_sound()