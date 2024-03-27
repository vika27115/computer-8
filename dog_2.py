class Dog:
  name = 'unknown'

  def __init__(self, bread, speed):
    self.is_walked = False 
    self.bread = bread
    self.speed = speed

  def walk(self):
    print(f'dog {self.name} walks')
    self.is_walked = True 

class DogSpike(Dog):
   name = 'Spike'
    
def run(self):
     print(f'dog {self.name} is running {self.speed} km\h')


class DogMike(Dog):
   name = 'Mike'

my_dog = DogSpike('bulldog', 12)
friends_dog = DogMike 

print('my dog name:', my_dog.name)
#print(my_dog.is_walked)
# my_dog.walk()
print('friends dog name;', friends_dog.name)

my_dog = DogSpike('bulldog', 12)
friends_dog = DogMike('pitbull', 20)
print(f'my dog name is {my_dog.name}')
print(f'my dog speed is {my_dog.speed} km\h')
print(f'my dog`s dog name is {friends_dog.name}')
