import matplotlib.pyplot as plt
import numpy as np

def collect(xs): #function / class has to be called collect (if a class, __call__ method must be implemented)
    #anything within this function can be changed real time 
    ys = np.sin(xs)
    print(ys)
