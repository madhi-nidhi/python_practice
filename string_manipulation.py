
def count_case(string1):
    count_upper = 0
    count_lower = 0
    for i in string1:
        if i.isupper():
            count_upper = count_upper + 1
        elif i.islower():
            count_lower = count_lower + 1
    return(count_upper, count_lower)