import math
import timeit

import matplotlib.pyplot as plt
import numpy as np

from final_project_part1 import *

graph_sizes = [5, 10, 15, 20, 25]
times = []

for size in graph_sizes:
    G = create_random_negative_graph(size)
    start_time = timeit.default_timer()
    shortest_paths = mystery(G)
    end_time = timeit.default_timer()
    times.append(end_time - start_time)

log_sizes = [math.log10(size) for size in graph_sizes]
log_times = [math.log10(time) for time in times]

slope, _ = np.polyfit(log_sizes, log_times, 1)

plt.plot(log_sizes, log_times, "bo-")
plt.xlabel("Graph Size")
plt.ylabel("Execution Time")
plt.title(f"Execution Time vs. Graph Size (log/log plot) - Slope: {slope:.1f}")
plt.show()