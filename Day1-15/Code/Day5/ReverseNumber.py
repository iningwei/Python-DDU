"""
正整数反转
比如12345，反转后为54321
"""
num=int(input("输入正整数："))
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
print("反转后%d" % (rev))