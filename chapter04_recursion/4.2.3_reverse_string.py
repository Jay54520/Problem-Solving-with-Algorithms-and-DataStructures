def reverse_string(string):
    n = len(string)
    if len(string) == 1:
        return string[0]
    else:
        return reverse_string(string[1:]) + string[0]
        
print(reverse_string('string'))        