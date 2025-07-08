import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_steps = 200
edge = 0.1
std = 1.0

sample_paths = []
for _ in range(10):
    outcomes = edge + std * np.random.randn(n_steps)
    sample_paths.append(np.cumsum(outcomes))

plt.figure(figsize=(10, 6))
for path in sample_paths:
    plt.plot(path, alpha=0.7)

plt.axhline(0, color='k', linestyle='--', lw=1)
plt.title('Sample Paths of P/L with Positive Edge')
plt.xlabel('Hand/Trade Number')
plt.ylabel('Cumulative P&L')
plt.show()
