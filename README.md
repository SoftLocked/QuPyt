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
