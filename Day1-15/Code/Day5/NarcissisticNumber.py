"""
水仙花数
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，个、十、百位上的数字的立方和等于其自身
"""
for x in range(100,1000):
    bai=x//100
    shi=x%100//10
    ge=x%100%10
    if bai**3+shi**3+ge**3==x:
        print("%d是水仙花数" % (x))
