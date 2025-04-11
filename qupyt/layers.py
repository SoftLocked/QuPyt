import qupyt as qp
import numpy as np

def Input(num_bits):
    return qp.subroutines.n_kron(qp.states.ZERO, num_bits)

def N_Hadamard(state):
    return np.round(qp.subroutines.n_kron(qp.gates.H, int(np.log2(state.shape[0]))) @ state, 10)

def Custom(state, gate):
    return np.round(gate @ state, 10)

def Measure(state, bits):
    return qp.Qubit.partial_measure(state, bits)