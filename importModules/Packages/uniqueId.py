import uuid

# make a UUID based on the host ID and current time
print(uuid.uuid1())

print('1.----------------')

# make a UUID using an MD5 hash of a namespace UUID and a name
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))

print('2.----------------')

# make a random UUID
print(uuid.uuid4())

print('3.----------------')

# mkae a UUID using a SHA-1 hash of a namespace UUID and a name
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))

print('4.----------------')

# make a UUID from a string of hex digits (braces and hyphens ignored)
x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

# convert a UUID to a string of hex digits in standard form
print(str(x))

print('5.----------------')

# get the raw 16 bytes of the UUID
print(x.bytes)
