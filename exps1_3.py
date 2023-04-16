import matplotlib.pyplot as plt
import numpy as np

from dbalgos import *

total_experiments = 100
max_nodes = 50
max_weight = 5000
max_relaxations = 5
max_density = 1

d_approx = []
d_exact = []
b_approx = []
b_exact = []

for d in np.arange(0, max_density, 0.05):
    d_approx_sum = 0
    d_exact_sum = 0
    b_approx_sum = 0
    b_exact_sum = 0
    for _ in range(total_experiments):
        G = create_random_weighted_graph(max_nodes, max_weight, d)
        d_approx_sum += total_dist(dijkstra_approx(G, 0, max_relaxations))
        d_exact_sum += total_dist(dijkstra(G, 0))
        b_approx_sum += total_dist(bellman_ford_approx(G, 0, max_relaxations))
    d_approx.append(d_approx_sum/total_experiments)
    d_exact.append(d_exact_sum/total_experiments)
    b_approx.append(b_approx_sum/total_experiments)

d_diff = []
for i in range(len(d_approx)):
    d_diff.append(d_approx[i] - d_exact[i])

b_diff = []
for i in range(len(b_approx)):
    b_diff.append(b_approx[i] - d_exact[i])
    
plt.title("Average Distance from Exact vs. Density")
plt.plot(np.arange(0, max_density, 0.05), d_diff, label = "Dijkstra Approximation")
plt.plot(np.arange(0, max_density, 0.05), b_diff, label = "Bellman-Ford Approximation")
plt.xlabel("Density")
plt.ylabel("Average Distance from Exact")

plt.legend()
plt.show()