import os

path = input("请输入文件路径:")
file_list = os.listdir(path)
n = 0
for i in file_list:
    oldName = path + os.sep + file_list[n]
    newName = path + os.sep + 'a' + str(n + 1) + '.jpg'
    os.rename(oldName, newName)
    print(oldName, '====>', newName)
