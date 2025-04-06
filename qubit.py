import numpy as np
from collections import defaultdict

class Qubit:
    
    @staticmethod
    def partial_measure(state, meas_qubits):
        n_qubits = int(np.log2(state.shape[0]))
        probs = defaultdict(float)
        post_states = defaultdict(lambda: np.zeros_like(state, dtype=complex))

        for i in range(2 ** n_qubits):
            amp = state[i]
            bits = format(i, f'0{n_qubits}b')
            outcome = ''.join([bits[q] for q in meas_qubits])
            probs[outcome] += np.abs(amp)**2
            post_states[outcome][i] = amp

        states = list(probs.keys())

        measured_state = states[np.random.choice(len(states), p=[i[0] for i in probs.values()])]

        
        norm = np.sqrt(probs[measured_state])
        if norm > 0:
            post_states[measured_state] /= norm

        return measured_state, post_states[measured_state]

    @staticmethod
    def checkValid(qb):
        n = qb.shape[0]
        return (n & (n - 1)) == 0 and sum(np.square(qb)) == 1