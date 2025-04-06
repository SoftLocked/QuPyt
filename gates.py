import numpy as np

X = np.array(
    [[0, 1],
     [1, 0]]
)

Y = np.array(
    [[0, -1j],
     [1j, 0]]
)

Z = np.array(
    [[1, 0],
     [0, -1]]
)

H = (1/np.sqrt(2)) * np.array(
    [[1, 1],
     [1, -1]]
)

def R(theta):
    return np.array(
    [[np.cos(theta), -np.sin(theta)],
     [np.sin(theta), np.cos(theta)]]
)

S = np.array(
    [[1, 0],
     [0, 1j]]
)

T = np.array(
    [[1, 0],
     [0, np.exp(1j * np.pi / 4)]]
)

def P(a):
    return np.array(
    [[1, 0],
     [0, np.exp(2 * np.pi * 1j / np.power(2,a))]]
)

I = np.eye(2)