from math import exp as e,sin,cos,pi


def get_roots(fx,dpoints):
    a=0
    b=a+0.2
    f_a=eval(fx.replace('x','a'))
    f_b=eval(fx.replace('x','b'))
    while (f_a<0 and f_b<0) or (f_a>0 and f_b>0):        
        a=b
        b+=0.2
        f_a=eval(fx.replace('x','a'))
        f_b=eval(fx.replace('x','b'))

    while True:
        c=(a*f_b-b*f_a)/(f_b-f_a)
        f_c=eval(fx.replace('x','c'))
        if (f_a<0 and f_c<0) or (f_a>0 and f_c>0): a=c
        else: b=c
        f_a=eval(fx.replace('x','a'))
        f_b=eval(fx.replace('x','b'))
        if abs(f_c) < float(f'0.{"0"*(int(dpoints))}9'): return f'{c} is the root with value {f_c}'

    
fx=input('equation: ')
dpoint=input('dpoints: ')

print(get_roots(fx,dpoint))




