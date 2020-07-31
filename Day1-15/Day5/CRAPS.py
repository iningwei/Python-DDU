"""
CRAPS
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
    玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
    玩家第一次如果摇出2点、3点或12点，庄家胜；
    其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
    如果玩家摇出了第一次摇的点数，玩家胜；
    其他点数，玩家继续要骰子，直到分出胜负。
"""

#引入随机数
from random import randint

dice1 =randint(2,12)
print("第一次摇出点数:%d" % (dice1))
if dice1 == 7 or dice1 == 11:
    print("You win!")
elif dice1 == 2 or dice1 == 3 or dice1 == 12:
    print("you lost!")
else:
    while True:
        diceNew = randint(2, 12)
        print("继续摇，点数:%d" % (diceNew))
        if diceNew == 7:
            print("you dice 7,you lost")
            break
        elif diceNew == dice1:
            print("you win!!!")
            break
