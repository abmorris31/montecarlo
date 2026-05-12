# Usage

To use montecarlo in a project, first import the package:

```python
import montecarlo
```
Then set a hamiltonian, where G is a graph object:

```python
montecarlo.IsingHamiltonian(G)
```

Finally, run for a temperature T with a specified number of samples (n_samples), and a specified number of burns (n_burn). It will return a list of energy values and a list of magnetization values. An example setup is shown below:

```python
E, M = mc.run(T=T, n_samples=100000, n_burn=100)
```