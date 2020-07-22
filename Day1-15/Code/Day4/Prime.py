"""
判断一个数是否是素数
只能被1和自身整除的大于1的整数是素数
"""
num = int(input("输入一个数："))
flag = True
if num > 1:
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            flag = False
            break
if flag:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
