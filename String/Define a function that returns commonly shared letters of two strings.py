def shared_letters(s1,s2):
    return len(set(s1)&set(s2))
print(shared_letters("hello","python"))