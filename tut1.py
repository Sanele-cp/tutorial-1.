import numpy as np
import pylab as pl

def vector(n):
	y = np.linspace(0,np.pi/2,n)
	return y

x = [10,30,100,300,1000]
for n in x:
	dx = np.pi/2/n
	y = np.linspace(0,np.pi/2,n)
	func = np.cos(y)
	integral = func.sum()*dx

	print("integral by simple method is",integral)

def simpson_method(n):
	dx = np.pi/2/(n-1)*2
	func = np.cos(y)
	even = func[2::2]
	odd = func[1:-1:2]
	total = np.sum(even)/3+np.sum(odd)*(2/3)+func[0]/6+func[-1]/6
	return total*dx
	print("integral by simpson_method is",total)


#simpson's rule in simple way
def f(x):
    return np.cos(x)

a = 0
b = 2
n = 100000

y1 = ((b-a)/(6*n))*(f(a) + f(b))

z = 0
for i in range(1,n,2): 
    y2 = ((b - a)/(3*n))*(4*(f(i*2/n))) #multiplied by 2 so that i will range to n instead of n/2 
    z += y2

x = 0
for i in range(1,n-1,2): 
    y3 = ((b - a)/(3*n))*(2*(f(i*2/n))) #multiplied by 2 so that i will range to n-1 instead of n-1/2 
    x += y3    

print("integral by simpson's rule is",y1 + z + x)


accuracy = simpson_method(11)
error = abs(accuracy-1)
print("accuracy is",accuracy)
print("error is",error)

z=[11,31,101,301,1001,3001,10001,3001,100001]  
z=np.array(z)
simpson_error=np.zeros(z.size)
simple_error=np.zeros(z.size)
for kk in range(z.size):
	n=z[kk]
	dx=np.pi/2/n
	x=np.linspace(0,np.pi/2,n)
	y=np.cos(x)
	Simple_Inte=y.sum()*dx
	simpson_error[kk]=np.abs(simpson_method(n)-1)
	simple_error[kk]=np.abs(Simple_Inte-1)
pl.plot(z,simple_error)
pl.plot(z,simpson_error)
ax=pl.gca()

ax.set_yscale('log')
ax.set_xscale('log')

pl.savefig("plot.pdf")
pl.show()
