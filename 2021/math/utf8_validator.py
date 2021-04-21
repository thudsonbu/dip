BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]

def utf8_validator(bytes):
  bytes_len = len(bytes)
  if bytes_len == 0 or bytes_len > 4:
    return False
  if bytes[0] & BYTE_MASKS[bytes_len] != BYTE_EQUAL[bytes_len]:
    return False
  for b in bytes[1:]:
    if b & 0b11000000 != 0b10000000:
      return False
  return True

print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True
