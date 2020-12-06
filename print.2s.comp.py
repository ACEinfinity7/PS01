
a = 29
b = ~ a

print(bytes([a]))

print(b)

print(b.to_bytes(2 , byteorder="big", signed=True))
