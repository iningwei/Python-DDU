"""
打印三角形图案
*
**
***
****
*****
******

     *
    **
   ***
  ****
 *****
******

     *
    ***
   *****
  *******
 *********
***********
"""
row = int(input("输入行数："))
# 第一种图案
for x in range(1, row+1):
    for j in range(1, x+1):
        print("*", end="")
    print()

# 第二种图案
for x in range(1, row+1):
    for j in range(row, 0, -1):
        if j > x:
            print(" ", end="")
        else:
            print("*", end="")
    print()

# 第三种图案
for x in range(1, row+1):
    for k in range(row-x, 0, -1):
        print(" ", end="")
    for p in range(2*x-1, 0, -1):
        print("*", end="")
    print()
