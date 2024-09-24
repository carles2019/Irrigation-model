import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['Monitoring', 'IMC', 'Funding', 'Participatory', 'Training', 'Business']
gfm = [34, 5, 4, 8, 4, 6]
imc = [11, 16, 4, 22, 7, 5]
small_h = [1, 0, 3, 0, 2, 0]
a1_a2 = [0, 0, 3, 0, 1, 0]
bot = [0, 0, 0, 0, 0, 0]
co_m = [0, 0, 0, 0, 0, 0]
flid = [3, 0, 0, 1, 2, 1]

# Grouping the data
bar_width = 0.1
x = np.arange(len(categories))

# Create the grouped bar chart
plt.figure(figsize=(12,6))
plt.bar(x - (3 * bar_width), gfm, width=bar_width, label='GFM', color='blue')
plt.bar(x - (2 * bar_width), imc, width=bar_width, label='IMC', color='orange')
plt.bar(x - bar_width, small_h, width=bar_width, label='Small H', color='green')
plt.bar(x + bar_width, a1_a2, width=bar_width, label='A1 & A2', color='red')
plt.bar(x + (2 * bar_width), bot, width=bar_width, label='BOT', color='purple')
plt.bar(x + (3 * bar_width), co_m, width=bar_width, label='Co.M', color='cyan')
plt.bar(x + (4 * bar_width), flid, width=bar_width, label='FLD.', color='magenta')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Analysis of Needs') # Updated title
plt.xticks(x, categories)
plt.legend()

# Show grid and plot
plt.grid(axis='y')
plt.tight_layout()
plt.show()