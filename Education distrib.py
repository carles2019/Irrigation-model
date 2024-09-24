import numpy as np
import matplotlib.pyplot as plt

# Data
education_groups = ['N/A', 'Primary', 'ZJC', 'O Level', 'A Level', 'Diploma', 'Degree', 'Postgraduate']
female = [2, 9, 18, 50, 1, 1, 0, 1]
male = [5, 10, 18, 40, 1, 3, 2, 3]

# Grouping the data
bar_width = 0.35
x = np.arange(len(education_groups))

# Create the grouped bar chart
plt.figure(figsize=(10,6))
plt.bar(x - bar_width/2, female, width=bar_width, label='Female', color='red')
plt.bar(x + bar_width/2, male, width=bar_width, label='Male', color='blue')

# Adding labels and title
plt.xlabel('Education Groups')
plt.ylabel('Frequencies')
plt.title('Frequencies of Male & Female Education Groups') # Title of the graph
plt.xticks(x, education_groups)
plt.legend()

# Show grid and plot
plt.grid(axis='y')
plt.tight_layout()
plt.show()