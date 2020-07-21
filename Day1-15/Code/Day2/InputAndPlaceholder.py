"""
使用input()接收键盘输入(字符串)
使用int()函数强转字符串
使用print()输出带占位符的字符串
%d 整数占位符、%f 浮点数占位符、%% 百分号
"""
a=int(input("a="))
b=int(input("b="))
print("%d + %d = %d" % (a,b,a+b))
print("%d / %d = %f " % (a,b,a/b))
print("%d // %d = %d " % (a,b,a//b))
print("%d %% %d = %d " % (a,b,a%b))