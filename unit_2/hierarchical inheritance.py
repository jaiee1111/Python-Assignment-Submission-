# hierarchical inheritance:

# base class 
class parent:
    def func1(self):
        print("this function is in parent class.")
        
# derived class 1
class child1(parent):
    def func2(self):
        print("this function is in child 1.")
        
# derive class 2 
class child2(parent):
    def func3(self):
        print("this function is in child2.")
        
#driver's code
object1=child1()
object2=child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

