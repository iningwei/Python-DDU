"""
输出100以内所有的素数
素数指的是只能被1和自身整除的正整数（不包括1）。
"""
for x in range(2, 100):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
            break
    if flag == True:
        print("%d是素数" % (x))
print("end")
