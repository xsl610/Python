from copy import deepcopy, copy

print([x for x in range(0, 10)])

print([x * x for x in range(0, 10)])

print("-" * 40)

tup1 = (50,)

for x in (12, 23, 45): print(x, end=' ')

dict = {'a': 1, 'b': 2, 'c': 3}
print(dict)

s1 = set('hello China!')
print(s1)

s1.add('hhh')
print(s1)

print("-" * 40)

s1.remove('hhh')
print(s1)

s1.discard(' ')
print(s1)

s1.clear()
print(s1)

print("*" * 40)

s2 = set(['a', 'b', 'c', 'd', 'e', 'f'])
s3 = set(['d', 'e', 'f', 'g', 'h', 'i'])
print('交集：', s2 & s3)
print('交集：', s2.intersection(s3))

print('并集：', s2 | s3)
print('并集：', s2.union(s3))

print('差集：', s2.difference(s3))
print('差集：', s2 - s3)

print('对称差集：', s2.symmetric_difference(s3))
print('对称差集：', s2 ^ s3)

list1 = [1, 2, ['a', 'b']]
list2 = deepcopy(list1)
print(id(list1) == id(list2))
list2[0] = 'a1'
list2[2][0] = 'b1'
print(list1, list2)
print("*" * 40)

list3 = [1, 2, ['a', 'b']]
list4 = copy(list1)
print(id(list1) == id(list2))
list4[0] = 'a1'
print(list3, list4)
list4[2][0] = 'b1'
print(list1, list2)

print("*" * 40)

x = 3
print(id(x))
x += 2
print(id(x))


