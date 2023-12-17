#%%
# چندک
import matplotlib.pyplot as plt
import numpy as np

y_data = [10, 15, 18, 20, 22, 25, 28, 30, 35, 40]

N = len(y_data)
x_data = [(i - 0.5) / N for i in range(1, N + 1)]
print(x_data)

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)

q1 = np.percentile(y_data, 25)
q3 = np.percentile(y_data, 75)
median = np.median(y_data)

plt.scatter([0.25, 0.5, 0.75], [q1, median, q3], color='red', marker='o')
plt.annotate(f"Q1: {q1:.2f}", (0.25, q1), textcoords="offset points", xytext=(0, 5), ha='center')
plt.annotate(f"Median: {median:.2f}", (0.5, median), textcoords="offset points", xytext=(0, 5), ha='center')
plt.annotate(f"Q3: {q3:.2f}", (0.75, q3), textcoords="offset points", xytext=(0, 5), ha='center')

plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Data')
plt.title('QQ Plot')

plt.show()
# %%
