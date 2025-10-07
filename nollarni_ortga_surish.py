nums = [0,1,0,3,12]

 
def moveZeroes(x):
    lastNonZero = 0
    for i in range(len(x)):
        if x[i] != 0:
            x[lastNonZero] = x[i]
            lastNonZero += 1
    for i in range(lastNonZero, len(x)):
        x[i] = 0
    return x


print(moveZeroes(nums))
