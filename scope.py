#scope - what variables do I have access to?

if True:
  x=10

def some_func():
  total=100

print(x)

#scope follow this order:
#1- start with locals
#2- parent local?
#3- global
#4- built in python functions por ej sum()