"""
华氏温度转摄氏温度
c=(f-32)/1.8
"""

f=float(input("输入华氏温度："))
c=(f-32)/1.8
print("1------>%.1f华氏度=%.1f摄氏度" % (f,c))
print(f"2------>{f:.1f}华氏度={c:.1f}摄氏度")