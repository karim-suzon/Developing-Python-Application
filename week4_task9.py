#Program calculates the exponential value(base and exponent are given in variable).Base can be a real number,exponent is a whole number.
#Use a loop

#print(2**3)     # 2^3 = 2**3 same  here 2 is base and 3 is exponent

def cal_exponent_val(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result= result * base_num
    return result

print(cal_exponent_val(2,3))