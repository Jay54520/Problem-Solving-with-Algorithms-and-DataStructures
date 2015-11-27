# Find a greatest common divisor
def gcd(m, n):
    while m % n != 0:
        old_m = m 
        old_n = n 
        
        m = old_n 
        n = old_m % old_n
    return n 

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(self.num, "/", self.den)
    
    # When need to convert to str
    def __str__(self):
        return str(self.num) + "/" + str(self.den)    
    
    # f1 + f2
    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num 
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    # f1 - f2 
    def __sub__(self, other_fraction):
        new_num = self.num*other_fraction.den-self.den*other_fraction.num 
        new_den = self.den*other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
        
    # f1 * f2 
    def __mul__(self, other_fraction):
        new_num = self.num*other_fraction.num 
        new_den = self.den*other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
        
    # f1 / f2 
    def __truediv__(self, other_fraction):
        new_num = self.num*other_fraction.den 
        new_den = self.den*other_fraction.num 
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
        
    # f1 < f2
    def __lt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        other_num = other_fraction.num * self.den
        return first_num < other_num
    
    # f1 > f2
    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        other_num = other_fraction.num * self.den
        return first_num > other_num
    
    # Compare two objects and return boolean
    def __eq__(self, other):
        first_num = self.num * other.den
        other_num = other.num * self.den
        return first_num == other_num

print(gcd(20, 10))        
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
print(f1 - f2, f1 * f2, f1 / f2, f1 < f2, f1 > f2, f1 == f2)


