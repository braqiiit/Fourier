# -*- coding: utf-8 -*-
from sympy import simplify, sympify, symbols, parse_expr

'''
The function fourierPoly takes the truth table of a real-valued or Boolean-valued
function on n bits and outputs its Fourier expansion.

n:  number of input bits
tt: array of arrays;
    represents the truth table; 2^n rows and (n+1) columns;
    the last column is the value of the function (it can take real valued numbers)
'''
def fourierPoly(n, tt):
    chunks = []
    for row in tt:
        value = row[n]
        chunks.append("({0})(".format(value))
        for i in range(n):
            if row[i]==-1:
                chunks.append("((1-x_{0})/2)".format(i+1))
            else:
                chunks.append("((1+x_{0})/2)".format(i+1))

        chunks.append(")")
        chunks.append(" + ")
    expr = ''.join(chunks[:-1])
    return simplify(parse_expr(expr, transformations="all")), expr

## Example 1: AND on 2 bits
tt =  [[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,-1]]
simpexpr,expr = fourierPoly(2,tt)
print('Interpolating polynomial: {}'.format(expr))
print('-----\n')
print('Simplified Expression: {}'.format(simpexpr))
print('-----\n')
for val in tt:
    print(val)
    print(simpexpr.evalf(1,subs={'x_1':val[0],'x_2':val[1]}))

## Majority on 3 bits
tt =  [
    [1,1,1,1],
    [1,1,-1,1],
    [1,-1,1,1],
    [1,-1,-1,-1],
    [-1,1,1,1],
    [-1,1,-1,-1],
    [-1,-1,1,-1],
    [-1,-1,-1,-1]
]
simpexpr,expr = fourierPoly(3,tt)
print('Interpolating polynomial: {}'.format(expr))
print('-----\n')
print('Simplified Expression: {}'.format(simpexpr))
print('-----\n')
for val in tt:
    print(val)
    print(simpexpr.evalf(1,subs={'x_1':val[0],'x_2':val[1],'x_3':val[2]}))