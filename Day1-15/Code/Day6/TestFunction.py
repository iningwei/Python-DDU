"""
函数
可选参数、可变参数
"""
from random import randint


def roll_dice(n=2):
    total = 0
    for i in range(1, n+1):
        total += randint(1, 6)    
    print("投%d次骰子，总点数：%d" % (n, total))

if __name__ == '__main__':
    roll_dice()
    roll_dice(1)
    roll_dice(5)


def add(a=0, b=0, c=0):
    return a+b+c

if __name__ == '__main__':
    print("--->%d" % (add()))
    print("--->%d" % (add(1)))
    print("--->%d" % (add(1,2)))
    print("--->%d" % (add(b=10)))
    print("--->%d" % (add(a=2,c=5)))

def add(*args):
    total=0
    for x in args:
        total+=x
    return total

if __name__ == '__main__':
    print("--->%d" % add(1,2,3,4,5))

def add2(a,b):
    return a+b

if __name__ == '__main__':    
    print("--->%d" % (add2()))
