def isPal(s):
    s = "".join(e for e in s if e.isalnum())
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])
        
print(isPal("reviled did I live, said I, as evil I did deliver"))

print(isPal("Go hang a salami; I'm a lasagna hog."))
print(isPal("radar"))
print(isPal(""))        