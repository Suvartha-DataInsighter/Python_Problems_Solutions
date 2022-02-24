class Parent:
    def Transportation(self):
        print("Bike")
class child(Parent):
    def Transportation(self):
        print("Car")
c=child()
c.Transportation()