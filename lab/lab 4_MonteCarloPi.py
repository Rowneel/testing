import random

def isInside_boundry(x,y):
    if x**2 + y**2 - 16< 0:
        return True
    else:
        return False

def approximate_pi(num_of_drops):
    num_inside = 0

    for _ in range(num_of_drops): 
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)
        if (isInside_boundry(x,y) == True):
            num_inside += 1
  
    return (4*num_inside)/num_of_drops


drops = 2000
pi_approximation = approximate_pi(drops)
print(f"The approximate value of PI with {drops} pin drops is {pi_approximation}")
