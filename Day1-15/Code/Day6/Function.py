from random import randint

def roll_dice(n=2):
    total = 0
    for i in range(1, n+1):        
        total += randint(1, 6)
    print("投%d次骰子，总点数：%d" % (n,total))

roll_dice()
roll_dice(1)
roll_dice(5)