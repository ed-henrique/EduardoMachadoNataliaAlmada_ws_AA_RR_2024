import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv("results.csv", sep=";")

df[['Type', 'Size']] = df['Entrada'].str.split('-', expand=True)
df['Size'] = df['Size'].astype(int)

# Quadratic curve data
x_quad = np.logspace(1, 5, num=100)
y_quad = (x_quad / 1e5) ** 2

# Plotting the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Size', y='Tempo', hue='Type', marker='o', legend='full')
plt.plot(x_quad, y_quad, label='Quadratic Curve (x^2)', color='black', linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Performance on Different Input Types')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
