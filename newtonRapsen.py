from sympy import *
import numpy as np
from math import exp as e,sin,cos,pi
def rapsen(f_x,x0,dpoints):
    my_symbols = {'x': Symbol('x', real=True)}
    g_x=str(diff(parse_expr(f_x, my_symbols)))
    while True:
        x1 = x0 - eval(f_x.replace('x','x0'))/eval(g_x.replace('x','x0'))
        if abs(eval(f_x.replace('x','x1'))) < float(f'0.{"0"*(int(dpoints))}9') or abs(x1-x0)<0.001: return f"{x1} is the root with value {eval(f_x.replace('x','x1'))}"
        x0=x1

print(rapsen(input('equation: '),float(input('first guesss: ')),int(input('decimal points: '))))
