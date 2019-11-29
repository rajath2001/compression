def padding(string):
    # adding extra zeros at make it divisible by 8 and storing that extra info
    num_zero = 8 - len(string) % 8
    for i in range (num_zero) :
        string += '0'
    
    start = "{0:0=8b}".format(num_zero)
    # print start
    start = start + string
    return start