import numpy as np
import matplotlib.pylab as plt

# creating an array of evenly spaced number from 0 to 200 
n = np.linspace(0,199,200)    
         
# defining the function x(n) 
def x(n): 
    e = eval(f)  
    return e 

# giving instructions to the user to avoid errors
print('NOTE: Please use np. instead of math. \n')
print('Example: np.sin or np.pi')
f = (input("Please input the function x(n): "))   
 
# using for loop for the piece-wise function y(n)
for i in range(0,200):
    if i <= 9:
        y = (-1.5 * x(n)) + (2 * x (n + 1)) - (0.5 * x(n + 2))
    elif i <= 198:
        y = (0.5 * x(n + 1)) - (0.5 * x(n - 1))
    else:
        y = (1.5 * x(n)) - (2 * x(n - 1)) + (0.5 * x(n - 2))
        

# plotting the graphs of the 2 functions
plt.plot(x(n), "y-", label = "x(n)")
plt.plot(y, "b-", label = "y(n)")

# adding grids and setting the limit for x and y-axis
plt.grid(True)
plt.xlim(0,200)
plt.ylim(-1,1)

# describing the graph
plt.xlabel('values of n')
plt.ylabel('output')
plt.legend()
plt.show
