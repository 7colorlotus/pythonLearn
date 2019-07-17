# -*- coding:utf-8 -*-
import importlib,sys

importlib.reload(sys)

from pyDes import *
from binascii import b2a_hex, a2b_hex

# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = des(b"DESCRYPT", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

data = '98335433'
KEY = "6fd4b7f4"    #密钥
IV = "138316236115"     #偏转向量
# 使用DES对称加密算法的CBC模式加密
k = des(b"DESCRYPT", CBC, b"\r\x08\x03\x10\x17\x06\x0b\x05", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print(b2a_hex(d))
print ("Decrypted: %r" % k.decrypt(d))
