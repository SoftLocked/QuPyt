import numpy as np

##################################################
# Single-Qubit States
##################################################

ZERO = np.array(
    [[1],
     [0]]
)

ONE = np.array(
    [[1],
     [0]]
)

PLUS = np.array(
    [[1/np.sqrt(2)],
     [1/np.sqrt(2)]]
)

MINUS = np.array(
    [[1/np.sqrt(2)],
     [-1/np.sqrt(2)]]
)

##################################################
# Bell Pairs
##################################################

PHI_PLUS = np.array(
    [[1/np.sqrt(2)],
     [0],
     [0],
     [1/np.sqrt(2)]]
)

PHI_MINUS = np.array(
    [[1/np.sqrt(2)],
     [0],
     [0],
     [-1/np.sqrt(2)]]
)

PSI_PLUS = np.array(
    [[0],
     [1/np.sqrt(2)],
     [1/np.sqrt(2)],
     [0]]
)

PSI_MINUS = np.array(
    [[0],
     [1/np.sqrt(2)],
     [-1/np.sqrt(2)],
     [0]]
)