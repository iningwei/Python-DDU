"""
计算两个整数的最大公约数(Greatest Common Divisor)和最小公倍数(Lowest Common Multiple)
定理：整数a和整数b, 有 a*b=GCD*LCM
"""
a=int(input("输入数a:"))
b=int(input("输入数b:"))
#----------->我的解法
#计算最大公约数
c1=a
gcd=1
if a<b:
    c1=b
for x in range(1,c1+1):
    if  a%x==0 and b%x==0:
        gcd=x
print("%d 和 %d 的最大公约数为：%d" % (a,b,gcd))
#计算最小公倍数
print("%d 和 %d 的最小公倍数为：%d" % (a,b,a*b//gcd))
