#6.Take a look at python.org site. Array methods are presented here:
# https://docs.python.org/3/tutorial/datastructures.html
#Give your own examples of using those metods.

a = [3, 10, -2]

print(a)
# result : [3, 10, -2]
a.append(1)    # adding 1 into the list
print(a)
# result: [3, 10, -2, 1]
a.append('hello')   # adding a string into the list
print(a)
# result : [3, 10, -2, 1, 'hello']
a.append([7,8, 'kokkola'])  # adding another list into the list
print(a)
# result : [3, 10, -2, 1, 'hello', [7, 8, 'kokkola']]
a.pop()  # deleting a item from list
print(a)
#result : [3, 10, -2, 1, 'hello']
a.pop()
print(a)
# retrive of specific number
print(a[1]) #1st index
print(a[0]) # index 0 is 3
#Insert an iteam at given position
a[0] = 100
print(a)
# result : [100, 10, -2, 1]
a[3] = "kokkola"
print(a)
# swapping two value
temp = a[0]
a[0] = a[3]
a[3] = temp
print(a)
# result : ['kokkola', 10, -2, 100]
# remove a specific iteam
a.remove('kokkola')
print(a)
# result : [10, -2, 100]
# list comprehensions
b = []
for x in a:
    b.append(x * 2)
print(b)
# result : [20, -4, 200]
d = []
for e in range(1,7):
    d.append(e * 2)
print(d)