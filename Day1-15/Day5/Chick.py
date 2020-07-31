"""
百钱百鸡问题(穷举法、暴力搜索法)
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""
cock = 0
hen = 0
chick = 0

for x in range(0, 21):
    for y in range(0, 34):
        cock = x
        hen = y
        chick = 100-x-y
        if chick % 3 == 0 and cock*5+hen*3+(chick//3) == 100:
            print("cock:%d,hen:%d,chick:%d" % (cock, hen, chick))
