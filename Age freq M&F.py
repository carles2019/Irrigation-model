import numpy as np
import matplotlib.pyplot as plt

# Data
age_groups = ['Below 25', '25-30', '31-40', '41-50', 'Above 50']
female = [1, 4, 8, 27, 42]
male = [3, 4, 12, 21, 42]

# Grouping the data
bar_width = 0.35
x = np.arange(len(age_groups))

# Create the grouped bar chart
plt.figure(figsize=(10,6))
plt.bar(x - bar_width/2, female, width=bar_width, label='Female', color='red')
plt.bar(x + bar_width/2, male, width=bar_width, label='Male', color='blue')

# Adding labels and title
plt.xlabel('Age Groups')
plt.ylabel('Frequencies')
plt.title('Frequencies of Male & Female Age Groups') # Title of the graph
plt.xticks(x, age_groups)
plt.legend()

# Show grid and plot
plt.grid(axis='y')
plt.tight_layout()
plt.show()