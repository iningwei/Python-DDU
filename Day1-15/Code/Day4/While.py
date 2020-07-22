"""
猜数字游戏
break跳出循环
"""

import random
target = random.randint(0, 100)
print("目标数字为%d" % target)
count = 0

while True:
    count = count+1
    value = int(input("输入数字："))
    if value < target:
        print("小了")
    elif value > target:
        print("大了")
    else:
        break
print("恭喜你猜对了，你一共猜了%d次" % count)            
