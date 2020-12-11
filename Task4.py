def convert_to_bytes(a, b):
    file = open(a, "wb+")
    b1 = bytes(b, 'utf-8')
    ba1 = bytearray(b1)
    file.write(ba1)
    file.read()
    file.close()
    return list(ba1)


print(convert_to_bytes("test.txt", 'Hello Python'))
