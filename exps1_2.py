import matplotlib.pyplot as plt
import numpy as np

from dbalgos import *

total_experiments = 25
max_nodes = 50
max_weight = 5000
max_relaxations = 5

d_approx = []
d_exact = []
b_approx = []
b_exact = []

for n in range(1, max_nodes):
    d_approx_sum = 0
    d_exact_sum = 0
    b_approx_sum = 0
    b_exact_sum = 0
    for _ in range(total_experiments):
        G = create_random_complete_graph(n, max_weight)
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

plt.title("Average Distance from Exact vs. Number of Nodes")
plt.plot(d_diff, label = "Dijkstra Approximation")
plt.plot(b_diff, label = "Bellman-Ford Approximation")
plt.xlabel("Number of Nodes")
plt.ylabel("Average Distance from Exact")

z = np.polyfit(range(len(d_diff)), d_diff, 1)
p = np.poly1d(z)
plt.plot(p(range(len(d_diff))), label = "Dijkstra Best Fit")

x = np.polyfit(range(len(b_diff)), b_diff, 1)
p = np.poly1d(x)
plt.plot(p(range(len(b_diff))), label = "Bellman-Ford Best Fit")

plt.legend()
plt.show()