#Võ Ngọc Duy - 2474802010071
from sympy import Symbol, symbols
x = Symbol('x')
f = x + x + x + 2
print("f =", f)
a = Symbol('Noi')
b = Symbol('Chim')
expr1 = 3*b + 7*a
print("expr1 =", expr1)
print("a.name:", a.name)
print("b.name:", b.name)
x, y, z = symbols('x y z')
a, b, c = symbols('a b c')
s = x**y + y**x
print("s =", s)
p = x * (x + 2*x)
print("p =", p)
p = (x + 2)*(y + 3)
print("p (chưa khai triển) =", p)
p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print("p (chưa khai triển) =", p)
p = x*(x - 2**2*x)
print("p (đơn giản hóa) =", p)
p = (x + 2)*(y + 3)
print("p.expand() =", p.expand())
