#Base64是一种用64个字符来表示任意二进制数据的方法。
#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

import base64
base64_str = base64.b64encode(b'binary\x00string')
print("base64_str:",base64_str)
base64_str_dec = base64.b64decode(base64_str)
print("base64_str_dec:",base64_str_dec)


#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
base64_str = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print("base64_str:",base64_str)
base64_urlsafe_str = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print("base64_urlsafe_str:",base64_urlsafe_str)
base64_urlsafe_dec = base64.urlsafe_b64decode(base64_urlsafe_str)
print("base64_urlsafe_dec:",base64_urlsafe_dec)



