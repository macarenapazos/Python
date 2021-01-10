basket = [1,2,3,4,5]
#adding elements
basket.append(6)
print(basket)

new_list = basket.append(9)
print(new_list) #return none

basket.insert(5,89)
print(basket)

basket.extend([100, 1001])
print(basket)

#removing elements

basket.pop() #removes the last element
basket.pop(2)

basket.remove(5) #removes the elements, works in place

new_list = basket.pop(2) 
print(new_list) #return 5 if we use the original one

basket.clear() #empty the list

#index

basket = ['a','b', 'c', 'd']
print(basket.index('b')) #retunt the index of the element

print('x' in basket) #return False
print('a' in basket) #return True

print(basket.count('d')) #count how many time d in the list




