import unittest

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        r = float(other.real**2 + other.imag**2)
        return Complex((self.real*other.real+self.imag*other.imag)/r, (self.imag*other.real-self.real*other.imag)/r)

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __neg__(self):   # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        return 'Complex' + str(self)

    def __pow__(self, power):
        raise NotImplementedError \
            ('self**power is not yet impl. for Complex')





class TestComplex(unittest.TestCase):

    def test_mul(self):
        a = Complex(6.0, 5.0)
        b = Complex(1.0, 1.0)
        c = a * b
        self.assertEqual(a.real*b.real - a.imag*b.imag, c.real, "multiplication real")
        self.assertEqual(a.imag*b.real + a.real*b.imag, c.imag, "multiplication real")


    def test_add(self):
        a = Complex(2, 5)
        b = Complex(5, 3)
        c = a + b
        self.assertEqual(a.real + b.real, c.real, "addition real")
        self.assertEqual(a.imag + b.imag, c.imag, "addition imaginary")
    def test_sub(self):
        a = Complex(8, 2)
        b = Complex(5, 6)
        c = a - b
        self.assertEqual(a.real - b.real, c.real, "addition real")
        self.assertEqual(a.imag - b.imag, c.imag, "addition imaginary")
    
def main():
    a = Complex(-3.0, 2.0)
    b = Complex(0.0, 5.0)
    c = Complex(0.0, -5.0)
    d = Complex(4.0, 5.0)
    e = Complex(-10.0, -5.0)
    f = a + b
    g = b - d
    h = c*e
    print("%s" %(f))
    print("%s" %(g))
    print("%s" %(h))
if __name__ == '__main__':
    main()

