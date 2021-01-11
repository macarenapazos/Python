#OOP

class BigObject:
  pass

obj1 = BigObject() #instanciate

print(type(obj1))

class PlayerCharacter:
  #class objecy Attribute
  membership=True
  def __init__(self, name, age):
    if(age>18):
      self.name = name #attributes
      self.age = age  

  def shout(self):
    print(f'my name is {self.name}')


@classmethod
def adding_things(cls,num1, num2):
  return num1+num2

player1 = PlayerCharacter('Hola', 23)
print(player1.name)
print(player1.shout())

