def get_roots(fx,a1,b1,precission):
    a=eval(fx.replace('x','a1'))
    b=eval(fx.replace('x','b1'))
    xa=(a1+b1)/2
    if a*b<0:
        loop_count=0
        while True:
            f_xa=eval(fx.replace('x','xa'))
            print(a1,xa,b1,f_xa,loop_count)       
            if (a<0 and f_xa<0) or (a>0 and f_xa>0): a1=xa
            else: b1=xa
            if abs(f_xa) < float(f'0.{"0"*(precission)}9'): return f'{xa} is the root with {f_xa}'
            xa=(a1+b1)/2
            loop_count+=1    
            if loop_count>50: break
    else: return 'no roots'

print(get_roots('x**x+x-100',2,4,1))
