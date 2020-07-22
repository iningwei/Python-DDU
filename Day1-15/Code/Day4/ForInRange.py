"""
0-100求和
range(b)取值范围是[0,b)
range(a,b)取值范围是[a,b)
range(a,b,2)取值范围是[a,b),且步长是2
"""

sum=0
for x in range(101):
    sum+=x
print('0-100:%d' % sum)