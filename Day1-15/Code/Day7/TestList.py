"""
列表 List
"""
list1 = [1, 3, 5, 7, 100]
print(list1)
print(list1*2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
list1[0] = 99
print(list1)
# 通过循环用下标遍历列表元素
for i in range(len(list1)):
    print(list1[i])
# 通过for循环遍历列表元素
for ele in list1:
    print(ele)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, ele in enumerate(list1):
    print(index, ele)

# 方法
print("--------------->方法")
print(list1)
list1.append(0)
list1.insert(1, 200)
list1.extend([300, 301])
list1 += [302, 303]
print(list1)
# 移除元素 (需要先判断是否存在，否则会抛出异常)
if 0 in list1:
    list1.remove(0)
# 删除指定位置元素
print(list1)
list1.pop(3)
print(list1)
# 清空
list1.clear()
print(list1)
