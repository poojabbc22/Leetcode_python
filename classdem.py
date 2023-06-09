class dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print("the dog breed is",self.name)
d=dog("rajpal")
d.bark()