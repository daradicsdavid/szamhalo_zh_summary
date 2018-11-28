import struct


#   Character       Type                Length
#   c               bytes of length 1 	1
#   ?               bool                1
#   h               short               2
#   i               int                 4
#   l               long                4
#   q               long long           8
#   e               float               2
#   f               float               4
#   d               double              8
#   s               bytes(char[])
def structExample():
    character_variable = b'c'
    bool_variable = True
    short_variable = 1
    integer_variable = 1
    long_variable = 1
    long_long_variable = 1
    short_float_variable = 1.0
    float_variable = 1.0
    double_variable = 1.0
    string_variable = 'Lorem ipsum test string'

    var = struct.pack('c?hilqefd', character_variable, bool_variable, short_variable, integer_variable, long_variable,
                      long_long_variable, short_float_variable, float_variable, double_variable)
    print("Packed struct:", var)

    (unpackedCharacterVariable, unpackedBoolVariable, unpackedShortVariable, unpackedIntegerVariable,
     unpackedLongVariable, unpackedLongLongVariable, unpackedShortFloatVariable, unpackedFloatVariable,
     unpackedDoubleVariable) = struct.unpack('c?hilqefd', var)

    print("Char:", character_variable, '->', "Unpacked char:", unpackedCharacterVariable)
    print("Bool:", bool_variable, '->', "Unpacked bool:", unpackedBoolVariable)
    print("Short:", short_variable, '->', "Unpacked short:", unpackedShortVariable)
    print("Integer:", integer_variable, '->', "Unpacked integer:", unpackedIntegerVariable)
    print("Long:", long_variable, '->', "Unpacked long:", unpackedLongVariable)
    print("Longlong:", long_long_variable, '->', "Unpacked longlong:", unpackedLongLongVariable)
    print("ShortFloat:", short_float_variable, '->', "Unpacked shortFloat:", unpackedShortFloatVariable)
    print("Float:", float_variable, '->', "Unpacked float:", unpackedFloatVariable)
    print("Double:", double_variable, '->', "Unpacked double:", unpackedDoubleVariable)

    print("String:", string_variable, "->", "Unpacked string:", unpack_string(pack_string(string_variable)))


def pack_string(string):
    binaryString = bytes(string, 'utf-8')
    return struct.pack("I%ds" % (len(binaryString),), len(binaryString), binaryString)


def unpack_string(packed_string):
    (i,), data = struct.unpack("I", packed_string[:4]), packed_string[4:]
    return data[:i].decode("utf-8")
