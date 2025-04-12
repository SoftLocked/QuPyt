# QuPyt
QuPyt is a python package to emulate and visualize quantum computations with a classical computer. It has a comprehensive set of quantum gates, states, and subroutines as well as as gate and circuit builders to make building concept quantum circuits (classical limit is about 15-20 qubits) as simple but powerful as possible on a classical machine, where computing is cheap compared to modern quantum machines.

## Installation
Using QuPyt is as simple as installing it from pip
```
$ pip install qupyt
```
__Note:__ QuPyt is a quantum wrapper over numpy arrays, meaning installing qupyt will install numpy if your environment does not already include it. Additionally, matplotlib will be installed for visualization purposes.

### Try your first QuPyt program
```
$ python
```
```python
>>> import qupyt as qp
>>> ket_plus = qp.states.PLUS
>>> measurement, new_state = qp.Qubit.partial_measure(ket_plus, [0])
>>> print(measurement, new_state)
0 [[1.+0.j]
 [0.+0.j]]
or
1 [[0.+0.j]
 [1.+0.j]]
```

Program initializes a qubit (numpy array) to ket_plus then measures that qubit to get a 0 measurement in the first (and only) qubit and a new state of ket 0 as that was what was measured. Alternatively, it could've measured a 1 in the first (and only) qubit and yield a new state of ket 1.

## Usage
### Qubit wrapper
QuPyt allows the user to work with familar numpy arrays for most computations. However, a quantum measurement is done by calling the static ``partial_measure`` function in the ``qp.Qubit`` class and passing in the numpy array along with a list of qubits the user wants to measure. This would look like the following:
```python
>>> import numpy as np
>>> import qupyt as qp
>>> state = np.array([[1],[0]])
>>> # Call partial_measure and pass in the state as well as the qubits you want measured
>>> # In this case, just the first, and only, qubit
>>> measurement, new_state = qp.Qubit.partial_measure(state, [0])
>>> print(measurement, new_state)
0 [[1.+0.j]
 [0.+0.j]]
```

### States
States in QuPyt are numpy column vectors that comply with the rules that constitute a qubit:
- Vector must be of size $2^n$ where $n$ is an integer
- The sum of the squares of all the vector values must be equal to 1
QuPyt accepts any numpy array that follows these two properties as a state. However, predefined states are also provided for common states in quantum computing:

```python
>>> import qupyt as qp
>>> qp.states.ZERO
array([[1],
       [0]])
>>> qp.states.ONE
array([[1],
       [0]])
>>> qp.states.PLUS
array([[0.70710678],
       [0.70710678]])
>>> qp.states.MINUS
array([[ 0.70710678],
       [-0.70710678]])
>>> qp.states.PHI_PLUS
array([[0.70710678],
       [0.        ],
       [0.        ],
       [0.70710678]])
>>> qp.states.PHI_MINUS
array([[ 0.70710678],
       [ 0.        ],
       [ 0.        ],
       [-0.70710678]])
>>> qp.states.PSI_PLUS
array([[0.        ],
       [0.70710678],
       [0.70710678],
       [0.        ]])
>>> qp.states.PSI_MINUS
array([[ 0.        ],
       [ 0.70710678],
       [-0.70710678],
       [ 0.        ]])
```

