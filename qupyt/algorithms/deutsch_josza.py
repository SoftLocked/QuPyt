import numpy as np
import qupyt as qp

def deutsch_josza(f, buffer):

    def deutsch_josza_Uf():
        nonlocal f
        nonlocal buffer
        dim = 2 ** (buffer+1)
        U = np.zeros((dim, dim))

        for i in range(dim):
            bits = format(i, f'0{buffer+1}b')
            x_bits = bits[:buffer]
            y_bit = bits[buffer]
            
            x_int = int(x_bits, 2)
            y_int = int(y_bit)
            
            output_y = y_int ^ f(x_int)
            
            out_bits = x_bits + str(output_y)
            input_idx = i
            output_idx = int(out_bits, 2)
            
            U[output_idx][input_idx] = 1

        return U
    
    intermediate = []

    state = qp.layers.Input(buffer+1) # Initializes circuit with n+1 qubits (all set to ket0)
    intermediate.append(state)

    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.subroutines.n_kron(qp.gates.I, buffer), qp.gates.X])) # Set the output qubit to ket1
    intermediate.append(state)
    
    state = qp.layers.N_Hadamard(state) # Apply Hadamard on all the qubits
    intermediate.append(state)
    
    state = qp.layers.Custom(state, deutsch_josza_Uf()) # Apply the Deutsch-Josza unitary to entire circuit
    intermediate.append(state)
    
    state = qp.layers.Custom(state, qp.subroutines.gate_builder([qp.subroutines.n_kron(qp.gates.H, buffer), qp.gates.I])) # Apply Hadamard to all the qubits except the output
    intermediate.append(state)
    
    state = qp.layers.Measure(state, list(range(buffer))) # Measure all qubits except the output qubit to get the result
    intermediate.append(state[1])

    return ('constant' if int(state[0]) == 0 else 'balanced', intermediate)