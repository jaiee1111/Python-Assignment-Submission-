# abstact class
class animal(ABC):
    def make_sound(self): 
      
# subclass 1 
class dog(animal):
    def make_sound(self): 
        return "bank!"
    
#subclass 2
class cat(animal):
    def make_sound(self):
        return"meow!"

#creating objects 
dog = dog()
cat = cat()

print(dog.make_sound())
print(cat.make_sound))

        