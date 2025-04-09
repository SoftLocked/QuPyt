import qupy as qp
import numpy as np

def func(i):
     arr = [1, 1]
     return arr[i]

print(qp.algorithms.deutsch(func))