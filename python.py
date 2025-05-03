
from sympy import *
from numpy import *
import math
from matplotlib.pyplot import *
x=symbols("x")
f=input("enter function:")
a=sympify(input("enter point:"))

f1=series(f,x,a,5).removeO()
f2=series(f,x,a,7).removeO()
f3=series(f,x,a,9).removeO()

pprint(f1)
pprint(f2)
pprint(f3)

fl=lambdify(x,f,"numpy")
f1l=lambdify(x,f1,"numpy")
f2l=lambdify(x,f2,"numpy")
f3l=lambdify(x,f3,"numpy")
xV=linspace(-5,5,200)
plot(xV,fl(xV),"blue",label=f"original f(x):{f}",linestyle="--")
plot(xV,f1l(xV),"red",label=f"expansion of order 5")
plot(xV,f2l(xV),"black",label=f"expansion of order 7")
plot(xV,f3l(xV),"green",label=f"expansion of order 9")

ylim(-3,3)
xlabel("x")
ylabel("y")
title("taylor series approximation")
legend()
grid()
show()
