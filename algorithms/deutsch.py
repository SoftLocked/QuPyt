import numpy as np
import qupy as qp

def deutsch(f):

    def deutsch_Uf(f):
        U = np.zeros((4, 4))
        for x in [0, 1]:
            for y in [0, 1]:
                input_index = 2*x + y
                output_y = y ^ f(x)
                output_index = 2*x + output_y
                U[output_index][input_index] = 1
        return U

    zero = np.array([[1], [0]])
    one = np.array([[0], [1]])

    init_state = np.kron(zero, one)

    after_hadamard = np.kron(qp.gates.H, qp.gates.H) @ init_state

    after_Uf = deutsch_Uf(f) @ after_hadamard

    hadamard_back = np.kron(qp.gates.H, qp.gates.I) @ after_Uf

    measured, new = qp.Qubit.partial_measure(hadamard_back, [0])

    return 'odd' if int(measured) == 1 else 'even'