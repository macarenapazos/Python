#al definir una función le damos parametros
def say_hello(name, emoji):
  print(f'helloooo {name} {emoji}')

#al llamarla le damos argumentos
say_hello('macu', '*') 

#we can define default parameters
def say_bye(name='Darth Vader', emoji='*'): 
  print(f'helloooo {name} {emoji}')

say_bye() #it will print darth vader

#keyword arguments

say_bye(emoji='RR', name='MAcu')
say_bye('hola')