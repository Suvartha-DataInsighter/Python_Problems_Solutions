def even_len(s):
    s=s.split(" ")
    for word in s:
        if(len(word)%2==0):
            print(word)
s="get even length charactes from the given string"
even_len(s)