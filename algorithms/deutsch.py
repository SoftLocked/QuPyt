import numpy as np
import qupy as qp

def deutsch(f):

    def deutsch_Uf(f):
        '''
        Define the Deutsch Unitary
        '''
        U = np.zeros((4, 4))
        for x in [0, 1]:
            for y in [0, 1]:
                input_index = 2*x + y
                output_y = y ^ f(x)
                output_index = 2*x + output_y
                U[output_index][input_index] = 1
        return U

    state = qp.layers.Input(2) # Initializes circuit with 2 qubits (all set to ket0)
    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.gates.I, qp.gates.X])) # Set the last qubit to ket1
    state = qp.layers.N_Hadamard(state) # Apply Hadamard on all the qubits to get ket+ and ket-
    state = qp.layers.Custom(state, deutsch_Uf(f)) # Apply the Deutsch unitary to entire circuit
    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.gates.H, qp.gates.I])) # Apply Hadamard to only the first qubit
    state = qp.layers.Measure(state, [0]) # Measure the first qubit to get the result

    return 'balanced' if int(state[0]) == 1 else 'constant' # If the measurement is ket1, the function is balanced. If ket0, the function is constant