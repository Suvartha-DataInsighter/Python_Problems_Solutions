def num_length(num):
    return sum(1 for i in str(num))
print(num_length(10000))