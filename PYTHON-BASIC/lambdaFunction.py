from functools import reduce

#  single line function
# lambda argument : expression

add =  lambda a,b : a + b
print(add(1,2))


square  = lambda x : x ** 2
print(square(2))

fruits = ['apple', 'banana', 'orange']
result = list (map(lambda fruit : fruit.upper(), fruits))
print(result)


nums = [1,2,3,4,5,6,7,8,9]
even = list (filter(lambda x : x % 2 == 0, nums))
print(even)

nums1 = [1,2,3,4,5,6,7,8,9]
sum =  reduce(lambda x,y : x + y, nums1)
print(sum)