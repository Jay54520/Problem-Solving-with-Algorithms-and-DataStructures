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
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError("The numbers must be int")
        if bottom == 0:
            raise ValueError("The bottom must not equal to 0")
        if top > 0 and bottom < 0:
            top = -top
            bottom = -bottom                   
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common
    
    def get_num(self):
        return self.num
        
    def get_den(self):
        return self.den
    
    def show(self):
        print(self.num, "/", self.den)
    
    # When need to convert to str
    def __str__(self):
        return str(self.num) + "/" + str(self.den) 
    
    # focus on making __str__ reasonably human-readable, 
    # and __repr__ as unambiguous as you possibly can
    def __repr__(self):
        return "Unambiguous"
    
    # f1 + f2
    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num 
        new_den = self.den * other_fraction.den        
        return Fraction(new_num, new_den)
    
    # x - y , 
    def __radd__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num 
        new_den = self.den * other_fraction.den        
        return Fraction(new_num, new_den)
    
    # x+=y
    def __iadd__(self, other_fraction):
        self.num = self.num*other_fraction.den + self.den*other_fraction.num 
        self.den = self.den * other_fraction.den        
        return Fraction(self.num, self.den)
        
    # f1 - f2 
    def __sub__(self, other_fraction):
        new_num = self.num*other_fraction.den-self.den*other_fraction.num 
        new_den = self.den*other_fraction.den
        return Fraction(new_num, new_den)
    
    # y is an instance of a class that has an __rsub__() method, 
    # y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.
    def __rsub__(self, other_fraction):
        new_num = self.num*other_fraction.den-self.den*other_fraction.num 
        new_den = self.den*other_fraction.den
        return Fraction(new_num, new_den)
        
    # f1 * f2 
    def __mul__(self, other_fraction):
        new_num = self.num*other_fraction.num 
        new_den = self.den*other_fraction.den        
        return Fraction(new_num, new_den)
        
    # f1 / f2 
    def __truediv__(self, other_fraction):
        new_num = self.num*other_fraction.den 
        new_den = self.den*other_fraction.num         
        return Fraction(new_num, new_den)
        
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
f2 = Fraction(4, 8)
f3 = f1 + f2
print(f3)
print(f1 - f2, f1 * f2, f1 / f2, f1 < f2, f1 > f2, f1 == f2)
print(f2.get_num(), f2.get_den())
f1 += f2
print(f1.__repr__())


