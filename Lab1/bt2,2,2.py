from sympy import Symbol, factor, pprint, init_printing
init_printing(order='rev-lex')
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**2 - 2*x*y + y**2
print("Biểu thức ban đầu:")
pprint(bieuthuc)
bieuthuc1 = factor(bieuthuc)
print("Biểu thức sau khi factor():")
pprint(bieuthuc1)
