
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# In[2]:

##bisection method n roots and single roots 

#single root
def bisec(g1,g2,tol,f):
    guess_1=g1
    guess_2=g2
    count =1 
    while (np.abs(guess_1-guess_2)>=tol):
          x= (guess_1+guess_2)/2.0
          product =f(guess_1)*f(x)
          if product > tol:
             guess_1= x
             count +=1
          else:
               if product < tol:
                 guess_2= x
                 count +=1
                 
      
        
    return print("The root is", x, "\n found at",count,"bisections")

# n root
def bisec_n(f,g1,g2,tol):
    guess_1=g1
    guess_2=g2
    count =1 
    while (np.abs(guess_1-guess_2)>=tol):
          x= (guess_1+guess_2)/2.0
          product =f(guess_1)*f(x)
          if product > tol:
             guess_1= x
             count +=1
          else:
               if product < tol:
                 guess_2= x
                 count +=1
    x= np.linspace(-20,20,10)
    plt.plot(x,f(x))
    plt.grid()
    plt.show()             
                
    return print("The root are", fsolve(f,[g1,g2]),"\n","found at bisections:", count)   


## regula falsi method single root and n roots

#single root
def false_pos(f,i1,i2,tol= 1e-6,max_pos=100):
    x_i= 0
    f_pos= 0
    if f(i1) * f(i2) < 0:
       for f_pos in range(max_pos+1):
            x_i= i2 -(i2-i1) / (f(i2)-f(i1)) * f(i2)
            if abs(f(x_i)) < tol: break
            elif f(i1) * f(x_i) < 0:
                 i2=x_i
            else:
                 i1=x_i 
    else:
          print("no roots exist within the interval") 
    
    
      
    return print("the root is ",x_i,"\n at epoach:", f_pos)

###place n root for regula falsi

##secant method single and n roots

#single root
def sec_meth (f,g1,g2,tol=1e-6,ep_max=100):
    for i in range(ep_max):
            x_i= g2 -(g2-g1) / (f(g2)-f(g1)) * f(g2)
            if abs(f(x_i)) < tol: break
            elif f(g1) * f(x_i) < 0:
                 g1=g2
                 g2=x_i
     
    
      
    return print("the root is ",x_i,"\n at epoach:", i)

### place secant method for n roots 


##Simple Iteration Methodd n roots single roots

#single root

def simp_iter(f,h,epochs = 50):
   #epochs = 50
   x_roots = []
   for epoch in range(epochs):
        x_guess = f(h)
        print(x_guess)
        if x_guess == 0:
            x_roots.append(h)
            break
        else:
              h+=1
   return print(f"The root is: {x_roots}, found at epoch {epoch}")

#n root
def simp_iter_n(f,h,epochs = 10):
  n_roots = 3
  x_roots = []
  end_epoch = 0


  for epoch in range(epochs):
    print(f(h))
    if np.allclose(0,f(h)):
      x_roots.append(h)
      end_epoch = epoch
      if len(x_roots)==n_roots:
        break
    h+=1

  return print(f"The root is: {x_roots}, found at epoch {end_epoch+1}")

##newton rhapson method

#single root
def newt(f,x,x_p,epochs = 100):
    f_prime= x_p
    root = None
    for epoch in range(epochs):
      x_prime = x - (f(x)/f_prime(x))
      if np.allclose(x, x_prime):
        root = x
        break
      x = x_prime
    return print("the root is ",root,"at epoch", epoch)

# n roots
def newt_n(f,range_guess,f_p,epoch=100):
   f_prime= f_p
   x_inits = range_guess
   roots = []
   for x_init in x_inits:
       x = x_init
       for epochs in range(epoch):
           x_prime = x - (f(x)/f_prime(x))
           if np.allclose(x, x_prime):
              roots.append(x)
              break
           x = x_prime
           np_roots = np.round(roots,3)
           np_roots = np.unique(np_roots)
   return (print("roots are ",np_roots,"found at",epochs))




