picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for image in picture:
  for x in image:
    if x == 0:
      print(' ',end='')
    elif x == 1:
      print('*', end='')
  print(end='\n')