import random

random.seed(12)
print(random.random())

random.seed(20)
print(random.random())

list2 = [20, 16, 10, 5]
random.shuffle(list2)
print(list2)

random.seed(12)
print(random.random())

print(random.choice([1, 2, 3, 4, 5, 6]))

str1 = "Hello world!"
print(str1[0:4])
print(str1[0:-2])
print(str1[0:-4])

print("---------------------")

print(str1[:6] + 'Python')
print(id(str1))

print("-" * 30)

print(r'\n')

print("I'm %s" % 'XuShiLiang')

print(str1.center(20, '&'))

print(str1.count('l', 0, len(str1)))

print("-" * 30)

print(str1.split())

print(str1.ljust(20, '*'))

print(str1.translate(str.maketrans("hld", "123")))

print('*' * 30)

print(str1.endswith('!'))

list1 = ["a", "b", "c", 78]

print(list1)
print(list1[1])

list1[3] = "d"
print(list1)
print("--" * 10)

list3 = ['a', 1, ['b', 6], 7]
print(list3[2][1])

list3.remove('a')
print(list3)

print(list2 + list3)

for i, v in enumerate(str1, 1):
    print(i, v)
