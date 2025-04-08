import numpy as np
import qupy as qp

def grover(f, buffer):

    def oracle():
        nonlocal buffer
        size = 2 ** buffer
        oracle = np.identity(size)
        for i in range(size):
            oracle[i, i] = -1 if f(i) == 1 else 1
        return oracle

    def diffusion():
        nonlocal buffer
        size = 2 ** buffer
        identity = np.identity(size)
        all_ones = np.ones((size, size))
        diffusion = 2 * all_ones / size - identity
        return diffusion
    
    
    intermediate = []

    state = qp.layers.Input(buffer) # Initializes circuit with n qubits (all set to ket0)
    intermediate.append(state)


    state = qp.layers.N_Hadamard(state) # Apply Hadamard on all the qubits
    intermediate.append(state)
    

    for i in range(int(np.floor(np.pi/4 * np.sqrt(np.power(2, buffer))))): # Repeat until probability of measuring intended answer is optimized
        state = qp.layers.Custom(state, oracle()) # Apply the oracle to entire circuit
        intermediate.append(state)

        state = qp.layers.Custom(state, diffusion()) # Apply the diffusion to entire circuit
        intermediate.append(state)

    measured = qp.layers.Measure(state, list(range(buffer))) # Measure all qubits to get the answer
    intermediate.append(measured[1])

    print(f"Grover's Found:  {int(measured[0], 2)} with {state[np.where(measured[1] == 1)[0]][0][0]*100:.02f}% certainty")

    return measured[0], intermediate