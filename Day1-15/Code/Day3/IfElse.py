"""
已知三角形三条边边长，判断是否能构成三角形，可以的话，计算其面积
面积计算公式为 海伦公式：https://zh.wikipedia.org/zh-hans/%E6%B5%B7%E4%BC%A6%E5%85%AC%E5%BC%8F
"""
a = float(input("边长a:"))
b = float(input("边长b:"))
c = float(input("边长c:"))

if a+b > c and b+c > a and a+c > b:
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print("面积为：%f" % (area))
else:
    print("无法构成三角形")
