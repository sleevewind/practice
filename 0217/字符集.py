# 使用内置函数 chr 和 ord, unicode字符编码
print(ord('a'))  # 97
print(chr(26666))  # 株

# 转化为指定字符集的结果
# gbk 一个汉字两个字节 utf8一个汉字3个字节
print('你'.encode('gbk'))  # b'\xc4\xe3' 0xc4e3
print('你'.encode('utf8'))  # b'\xe4\xbd\xa0' 0e4bda0
print(b'\xe4\xbd\xa0'.decode('utf8'))  # 你
