
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# In[2]:

##bisection method n roots and single roots 

def bisec(f,g1,g2,n_roots):
  epochs= 100
  interval= 50
  tol = 1.0e-06
  roots = []
  xpoint = []
  ypoint = []
  
  for i in range(interval): #Moving intervals
    g1+=0.25
    g2+=0.25
    xpoint.append(g1)
    ypoint.append(g2)
  
  for (g1,g2) in zip (xpoint,ypoint):
    y1, y2 = f(g1), f(g2)
    root = None
    end_bisect = 0
    if np.sign(y1) == np.sign(y2):
      pass #Root are not in this interval
    else:
      for bisect in range(epochs):
        midp = np.mean([g1,g2])
        y_mid = f(midp)
        y1 = f(g1)
        if np.allclose(0,y1, tol):
          root = g1
          roots.append(root)
          final_roots = np.unique(np.around(roots,3))
          final_roots = final_roots[:n_roots]
          end_epoch = bisect
          break
        if np.sign(y1) != np.sign(y_mid): #root is in first-half interval
          g2 = midp
        else: #root is in second-half interval
          g1 = midp 

  return print("The roots  {}, found at epoch: {} ".format(final_roots, end_epoch))
  
## regula falsi method single root and n roots

def false_pos(f,g1,g2,n_roots):
  epochs =100 
  interval = 50
  tol = 1.0e-06
  roots = []
  xpoint = []
  ypoint = []
 
  for i in range(interval):
    g1+=0.25
    g2+=0.25
    xpoint.append(g1)
    ypoint.append(g2)
  for (g1,g2) in zip (xpoint,ypoint):
    y1, y2 = f(g1), f(g2)
    root = None 
    pos = 0
    for pos in range(epochs):
        c = g2 - (f(g2)*(g2-g1))/(f(g2)-f(g1)) ##false root
        if np.allclose(0,f(c), tol):
          root = c
          roots.append(root)
          final_roots = np.unique(np.around(roots,3))
          final_roots = final_roots[:n_roots]
          break
        if np.sign(f(g1)) != np.sign(f(c)): g2,y2 = c,f(c)
        else: g1,y1 = c,f(c) 
  
  return print("The roots are {}, at pos: {} ".format(final_roots, pos))
    
 





#secant method for n roots and single root

def sec_meth(f,g1,g2,n_roots):

  epochs = 100
  interval = 50
  tol = 1.0e-06
  roots = []
  xpoint = []
  ypoint = []

  for i in range(interval):
    g1+=0.25
    g2+=0.25
    xpoint.append(g1)
    ypoint.append(g2)

  for (g1,g2) in zip (xpoint,ypoint):
    root = None
    end_epoch =  0
    for epoch in range(epochs):
      g3 = g2 - (f(g2)*(g2-g1))/(f(g2)-f(g1))
      if np.allclose(g2,g3): 
        root = g3
        roots.append(root)
        final_roots = np.unique(np.around(roots,3))
        final_roots = final_roots[:n_roots]
        end_epoch = epoch
        break
      else:
        g1,g2 = g2,g3

  return print("The roots  {}, found at epoch: {} ".format(final_roots, end_epoch))

  
       


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

def derivative(F,x,dx = 1e-6): 
  diff = F(x+dx)-F(x-dx)  
  return diff/(2*dx)

def newton(f,n_roots,epochs=100, tol = 1.0e-05,inits = np.arange(-5,5)):
  roots = []
  for init in inits:
    x=init
    for epoch in range(epochs):
      F_p = derivative(f,x)
      x_new = x - (f(x)/F_p)
      if np.allclose(x, x_new, tol):
        roots.append(x)
        final_roots = np.unique(np.around(roots,3))
        final_roots = final_roots[:n_roots]
        break
      x = x_new
  return print("The roots are {}, found at epoch: {} ".format( final_roots, epoch)) 


### simp 
   
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



