from random import *

randomNum = int(random() * 100)
guessCount = 0
while True:
    guessNum = input("请输入一个数：")
    if guessNum.isdigit():
        guessNum = int(guessNum)
    else:
        continue
    guessCount += 1
    if guessNum > randomNum:
        print('猜大了！')
        continue
    elif guessNum < randomNum:
        print('猜小了！')
        continue
    else:
        print('OK!!!')
        break
print('猜的数为：', guessNum)
print('猜的次数为：', guessCount)
