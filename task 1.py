more = [x + 1 for x in [1,2,3,4]]     # [1+1=2, 2+1=3, 3+1=4, 4+1=5]
print()                               # more = [2, 3, 4, 5]

def square(n:int) -> int:
    return n * n                           # n = [1*1 = 1, 2*2 = 4, 3*3 = 9, 4*4 = 16]
squares = [square(x) for x in [1,2,3,4]]   # squares = [1, 4, 9, 16] this reflects the multiplication of the function above
print()

def check(n:int) -> bool:
    return n > 2                             # 1 > 2 = False, 2 > 2 = False, 3 > 2 = True, 4 > 2 = True
answer = [x for x in range(5) if check(x)]   # answer = [3, 4]
print()

def inc(m:int) -> int:
    return m + 1                             # 3 + 1 = 4, 4 + 1 = 5


def check(n:int) -> bool:
    return n > 2                             # 1 > 2 = False, 2 > 2 = False, 3 > 2 = True, 4 > 2 = True


answer = [inc(x) for x in range(5) if check(x)]   # answer = [4, 5]
print()