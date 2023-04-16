import matplotlib.pyplot as plt

from dbalgos import *

total_experiments = 50
total_nodes = 50
max_weight = 5000
max_relaxations = 18

d_approx = []
d_exact = []
b_approx = []
b_exact = []

for k in range(max_relaxations):
    d_approx_sum = 0
    d_exact_sum = 0
    b_approx_sum = 0
    b_exact_sum = 0
    for _ in range(total_experiments):
        G = create_random_complete_graph(total_nodes, max_weight)
        d_approx_sum += total_dist(dijkstra_approx(G, 0, k))
        d_exact_sum += total_dist(dijkstra(G, 0))
        b_approx_sum += total_dist(bellman_ford_approx(G, 0, k))
    d_approx.append(d_approx_sum/total_experiments)
    d_exact.append(d_exact_sum/total_experiments)
    b_approx.append(b_approx_sum/total_experiments)


print("Dijkstra Approximation")
for i in range(len(d_approx)):
    if d_approx[i] == d_exact[i]:
        print(i)
        break
    
print("Bellman-Ford Approximation")
for i in range(len(b_approx)):
    if b_approx[i] == d_exact[i]:
        print(i)
        break

plt.title("Average Total Distance vs. Number of Relaxations")
plt.plot(d_approx, label = "Dijkstra Approximation")
plt.plot(b_approx, label = "Bellman-Ford Approximation")
plt.plot(d_exact, label = "Exact")
plt.xlabel("Number of Relaxations")
plt.ylabel("Average Total Distance")

plt.legend()
plt.show()