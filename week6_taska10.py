#10.Search for a value from an array.

def search(array, n):
    i = 0

    while i<len(array):
        if array[i] == n:
            return True
        i = i + 1
    return False


array = [2,3,4,5,10,11,12,15]
n = 10

if search(array,n):
    print("found")
else:
    print("not found")