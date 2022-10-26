# file_handle=open(r'E:\cz.txt','r+',encoding='utf8')
# file_handle.write("上网课")
# print(file_handle.read())

with open("E:/yzm.jpg", "rb") as file1, open("E:/yzm1.jpg", "wb") as file2:
    iBytes = file1.read()
    file2.write(iBytes)
