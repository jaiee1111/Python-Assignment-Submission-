# single inheritance:

#bace class 
class parent:
    def func1(self):
        print("this function is in parent class.")
        
#derived class 
class child(parent):
    def func2(self):
        print("this function is in child class.")
        
# driver's code
object=child()
object.func1()
object.func2()

