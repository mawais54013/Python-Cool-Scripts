# range examples

# normal range

def range1(num):
    return list(range(num))

print(range1(5))
# [0,1,2,3,4]
# print everything up to 5 but not including 5

def range2(num):
    return list(range(num, 10))

print(range2(5))
# [5,6,7,8,9]
# prints from 5 and up to 10 but not including 10

def range3(num1, num2, num3):
    return list(range(num1, num2, num3))

print(range3(0, 10, 2))
# [0,2,4,6,8]
# prints the evens because of the '2' up til 10

