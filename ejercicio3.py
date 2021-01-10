def highest_even(li):
  i=0
  for num in li:
    if num%2==0:
      if num > i:
        i=num
  return i
print(highest_even([0,2,3,4,80,11]))

def highest_even2(li):
  evens=[]
  for item in li:
    if item%2==0:
      evens.append(item)
  return max(evens)
print(highest_even2([0,2,3,4,80,11]))
