# *args **kwargs

def super_func(*args):
  return sum(args)

print(super_func(1,2,3,4,5))

def super_func2(*args, **kwargs):
  total=0
  for items in kwargs.values():
    total+=items
  return sum(args) + total

print(super_func2(1,2,3,4,5, num1=5, num2=10))

#rule: params, *args, default parameters, **kwargs (en ese orden)

