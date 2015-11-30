import re
import ipdb

def palindrome_checker(string):
    # 去除非字母
    if  isinstance(string, str):
        string = re.sub('[^A-Za-z]+', "", string)
        string = list(string)      

    if len(string) < 2:
        return True
    else:
        if string.pop(0) != string.pop():
            return False
        else:
            return palindrome_checker(string)
            
print(palindrome_checker('kayak'))            

            
        