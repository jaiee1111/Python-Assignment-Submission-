# multiple inheritance:

class mother:
    mothername=" "
    def mother(self):
        print(self.mothername)
    
#base class2 
class father:
    fathername=" "
    def father(self):
        print(self.fathername)
    
#derived class
class son(mother,father):
    def parents(self):
        print("mother:",self.mothername)
        print("father:", self.fathername)
        
#driver's code
s1=son()
s1.mothername="abc"
s1.fathername="xyz"
s1.parents()

