
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# In[2]:

##bisection method n roots and single roots 

def bisec(f, g1, g2, n_roots):
    epochs=100
    tol=1e-06
    y1, y2 = f(g1), f(g2)
    roots = []
    end_bisect = 0
    try:
      if np.sign(y1) == np.sign(y2):
          print("Root cannot be found")
      else:
          for bisect in range(epochs):
              midpoint = np.mean([g1,g2])
              y_mid = f(midpoint)
              y1 = f(g1)
              if np.allclose(0, y1, tol):
                  n_root = g1
                  roots.append(g1)
                  end_bisect = bisect
                  if len(roots) == n_roots: 
                    break
              if np.sign(y1) != np.sign(y_mid): 
                  g2 = midpoint
              else: 
                  g1 = midpoint 
          if len(roots) <= 1:
            print(f"Root is: {roots}, found at epoch {end_bisect}")
          elif len(roots) > 1:
            print(f"Roots are: {roots}, found at epoch {end_bisect}")
    except Exception as e:
      print("Error: ", e)

## regula falsi method single root and n roots

def false_pos(f, a, b,n_roots):
  tol=1e-06
  epochs=100
  y1, y2 = f(a),f(b)
  roots = [] 
  epoch = 0
  try:
    if np.allclose(0,y1): roots.append(a)
    elif np.allclose(0,y2): roots.append(b)
    elif np.sign(y1) == np.sign(y2):
      print("No root here")
    else:
      for epoch in range(epochs):
        c = b - (f(b)*(b-a))/(f(b)-f(a))
        if np.allclose(0,f(c), tol):
          roots.append(c)
          if len(roots) == n_roots:
            break
        if np.sign(f(a)) != np.sign(f(c)): b,y2 = c,f(c)
        else: a,y1 = c,f(c) 
    if len(roots) <= 1:
      print(f"The root is: {roots}, found at epoch {epoch}")
    elif len(roots) > 1:
      print(f"The roots are: {roots}, found at epoch {epoch}")
  except Exception as e:
    print("Error: ", e)
 

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

#secant method for n roots 

def secant_meth_n(f,n_roots,g1,g2,epochs=100,tol=4):
    n_roots = set([])
    try:
        if f(g1) == f(g2):
            print('\ncannot be computed\n\n')
        else:
            for epoch in range(epochs):
                g_new = g1 - f(g1)*(g2-g1)/( f(g2) - f(g1))
                print("Epoch Count: {}, g_new = {}".format(epoch,round(g_new,tol)))
                if np.allclose(g2,g_new): 
                    n_roots.add(g_new)
                    break
                g1 = g2
                g2 = g_new
            print('\nThe root is: {}, found at {} epochs\n'.format(round(g_new,tol),epoch))
            print("The roots found are:\n",n_roots)
    except Exception as Er:
        print("Error:", Er)


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
   
def samp(f,f_p):
    f_prime=f_p
    epochs = 100
    x_inits = np.arange(0,5)
    roots = []
    for x_init in x_inits:
        x = x_init
        for epoch in range(epochs):
            x_prime = x - (f(x)/f_prime(x))
            if np.allclose(x, x_prime):
               roots.append(x)
               break
      
    x = x_prime
    np_roots = np.array(roots)
    np_roots = np.round(np_roots,3)
    np_roots = np.unique(np_roots)
    return np_roots



