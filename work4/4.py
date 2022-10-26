with open("E:/yzm.jpg", "rb") as image_file1, open("E:/yzm1.jpg", "wb") as image_file2:
    iBytes = image_file1.read()
    image_byte_count = image_file2.write(iBytes)
    print("写入的字节数量是%d" % image_byte_count)
