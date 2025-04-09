import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import qupyt as qp

def grover(f, num_sols=1, buffer=10):

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


    state = qp.layers.N_Hadamard(state) # Apply Hadamard on all the qubits
    intermediate.append(state)
    

    for i in range(int(np.floor(np.pi/4 * np.sqrt(np.power(2, buffer)/num_sols)))): # Repeat until probability of measuring intended answer is optimized
        state = qp.layers.Custom(state, oracle()) # Apply the oracle to entire circuit
        intermediate.append(state)

        state = qp.layers.Custom(state, diffusion()) # Apply the diffusion to entire circuit
        intermediate.append(state)

    measured = qp.layers.Measure(state, list(range(buffer))) # Measure all qubits to get the answer

    print(f"Grover's Found:      {int(measured[0], 2)} with {state[np.where(measured[1] == 1)[0]][0][0]*100:.02f}% certainty")

    return measured[0], intermediate





def animate_grover(intermediate, BUFFER, MARKED_INDICES):

    def grover_basis(N, marked_indices):
        # Create |alpha⟩ (non-solution states)
        alpha = np.ones(N, dtype=complex)
        for idx in marked_indices:
            alpha[idx] = 0
        alpha /= np.linalg.norm(alpha)
        
        # Create |beta⟩ (solution state(s))
        beta = np.zeros(N, dtype=complex)
        for idx in marked_indices:
            beta[idx] = 1
        beta /= np.linalg.norm(beta)

        return alpha, beta

    def project_to_grover_plane(state, alpha, beta):
        proj_alpha = np.vdot(alpha, state)
        proj_beta = np.vdot(beta, state)
        return np.array([proj_alpha, proj_beta])
    
    alpha, beta = grover_basis(np.power(2, BUFFER), MARKED_INDICES)

    states_projected = np.array([project_to_grover_plane(i, alpha, beta) for i in intermediate])

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('Projection on |α⟩ (non-solution space)')
    ax.set_ylabel('Projection on |β⟩ (solution space)')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.set_title("Grover's Algorithm State Evolution")

    # Initialize the line objects for the animation
    line, = ax.plot([], [], 'bo-', label='State Vector', markersize=8)
    text = ax.text(0, 0, "", color="black", fontsize=12)

    # Initialize the plot
    def init():
        line.set_data([], [])
        text.set_text("")
        return line, text

    # Update function for animation
    def update(frame):
        x, y = states_projected[frame]
        line.set_data(states_projected[:frame+1, 0], states_projected[:frame+1, 1])
        text.set_text(f'Step {frame}')
        return line, text

    # Create animation
    ani = FuncAnimation(fig, update, frames=len(states_projected), init_func=init, blit=True, interval=100)

    #ani.save('grover.gif', writer='pillow', fps=5)
    
    plt.legend()
    plt.show()