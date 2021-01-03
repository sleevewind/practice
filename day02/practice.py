# 获取十六进制颜色 0xF0384E 的RGB值，以十进制形式打印
color = 0xF0384E
red = color >> 16
green = (color & 0x00ff00) >> 8
blue = color & 0x0000ff
print("red = ",hex(red))
print("green = ",hex(green))
print("blue = ",hex(blue))
