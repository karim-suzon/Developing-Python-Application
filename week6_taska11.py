#11.Calculates the square root of value 2 (create your own function).

def sqrt(N):
    if N < 0:
        print('Square root of negative number does not exist!')
        return
    else:
        print(f'Square root of number {N}: {N**0.5}')
        return
sqrt(2)