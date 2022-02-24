## The Python String encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
def str_encode(string):
# print string
    print('The string is:', string)
    print(string.encode("ascii", "replace"))
string = 'I love my family'
str_encode(string)
