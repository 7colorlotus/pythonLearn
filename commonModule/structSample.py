#struct模块来解决bytes和其他二进制数据类型的转换。
import struct
struct_byte = struct.pack('>I',10240099) #>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct_byte)

struct_unpack = struct.unpack('>I',struct_byte)
print(struct_unpack)

struct_unpack = struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80') #根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
print(struct_unpack)

