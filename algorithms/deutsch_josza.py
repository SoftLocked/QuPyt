import numpy as np
import qupy as qp

def deutsch_josza(f, n):

    def deutsch_josza_Uf(f, n):
        dim = 2 ** (n + 1)
        U = np.zeros((dim, dim))

        for i in range(dim):
            bits = format(i, f'0{n+1}b')
            x_bits = bits[:n]
            y_bit = bits[n]
            
            x_int = int(x_bits, 2)
            y_int = int(y_bit)
            
            output_y = y_int ^ f(x_int)
            
            out_bits = x_bits + str(output_y)
            input_idx = i
            output_idx = int(out_bits, 2)
            
            U[output_idx][input_idx] = 1

        return U

    zero = np.array([[1], [0]])
    one = np.array([[0], [1]])

    init_state = zero
    n_hadamard = qp.gates.H
    for i in range(n-1):
        init_state = np.kron(init_state, zero)
        n_hadamard = np.kron(n_hadamard, qp.gates.H)
    init_state = np.kron(init_state, qp.gates.H @ one)
    n_hadamard = np.kron(n_hadamard, qp.gates.I)

    after_hadamard = n_hadamard @ init_state

    after_Uf = deutsch_josza_Uf(f, n) @ after_hadamard

    hadamard_back = n_hadamard @ after_Uf

    measured, new = qp.Qubit.partial_measure(hadamard_back, [i for i in range(n)])

    return 'constant' if int(measured) == 0 else 'balanced'