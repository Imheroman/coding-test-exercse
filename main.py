line = "nice day"  # line = input()
encryption_key = "love"  # encryption_key = input()
encryption_line = list()
encryption_key_length = len(encryption_key)
Z_LOWERCASE_ALPHABET_ASCII = ord('z')

for line_index in range(len(line)):
    letter = ord(line[line_index])
    key = ord(encryption_key[line_index % encryption_key_length])

    if letter == ' ':
        continue

    value = letter - key

    print("letter: ", line[line_index], "/ encrypted: ", key)
    if letter - value < ord('a'):
        letter += Z_LOWERCASE_ALPHABET_ASCII

    letter -= value
    encryption_line.append(chr(letter))

print(encryption_line)

# for letter in line:
#     if letter == " ":
#         encryption_key_index += 1
#         pass
#
#     if
#
#     encryption_key_index %= encryption_key_length
#
#
#
#
#
#     encryption_key_index += 1
#     pass


"""
nice day
love
"""
