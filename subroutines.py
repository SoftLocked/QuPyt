import numpy as np

def n_kron(gate, n):
    result = gate
    for i in range(n-1):
        result = np.kron(result, gate)
    return result

def gate_builder(gates):
    if not gates:
        raise ValueError('Gate builder expects one or more gates')
    
    result = gates[0]
    for i in range(1, len(gates)):
        result = np.kron(result, gates[i])
    
    return result