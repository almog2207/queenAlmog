def firstNum(num1):
    for i in range(2,num1):
        num = 0
        if num1 % i == 0:
            return False
    return True

print(firstNum(5))

print()
def onnumbers():
    for i in range(1000):
        if firstNum(i):
            print(i)


onnumbers()
