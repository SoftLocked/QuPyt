import numpy as np
import qupyt as qp

def bernstein_vazirani(f, buffer):

    def bernstein_vazirani_Uf():
        nonlocal f
        nonlocal buffer
        dim = 2 ** (buffer + 1)
        U = np.zeros((dim, dim))

        for i in range(dim):
            bits = format(i, f'0{buffer+1}b')
            x_bits = bits[:buffer]
            y_bit = bits[buffer]
            
            x_int = int(x_bits, 2)
            y_int = int(y_bit)
            
            output_y = y_int ^ f(x_int, buffer)
            
            out_bits = x_bits + str(output_y)
            input_idx = i
            output_idx = int(out_bits, 2)
            
            U[output_idx][input_idx] = 1

        return U

    
    state = qp.layers.Input(buffer+1) # Initializes circuit with n+1 qubits (all set to ket0)
    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.subroutines.n_kron(qp.gates.I, buffer), qp.gates.X])) # Set the output qubit to ket1
    state = qp.layers.N_Hadamard(state) # Apply Hadamard on all the qubits
    state = qp.layers.Custom(state, bernstein_vazirani_Uf()) # Apply the Deutsch-Josza unitary to entire circuit
    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.subroutines.n_kron(qp.gates.H, buffer), qp.gates.I])) # Apply Hadamard to all the qubits except the output
    state = qp.layers.Measure(state, list(range(buffer))) # Measure all qubits except the output qubit to get the result

    return state[0]