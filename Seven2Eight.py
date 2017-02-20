# coding:utf-8
###DES算法中实际56比特的密钥，共7字节，在每个7比特的后面添加0，转化位标准的8字节的密钥

Key7 = raw_input("请以16进制方式输入7 字节的密钥（例如：2153d114e779b4）:\n")
print("Origin Key:", Key7)
a=bin(int (Key7,16))[2:].zfill(56)
#'00100001010100111101000100010100111001110111100110110100'
print a
c=''
for i in range(8):
    b= a[i*7:i*7+7]+'0'
    c += hex(int(b,2))[2:].zfill(2)
print ("New Key:",c)
