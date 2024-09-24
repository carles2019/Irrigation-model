import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['Moderate', '50 to 60%', '3000ha+', '7000ha']
gfm = [5, 6, 46, 1]
imc = [6, 16, 36, 2]
small_h = [2, 4, 0, 0]
a1_a2 = [4, 0, 0, 0]
bot = [3, 15, 8, 0]
co_m = [1, 0, 1, 0]
flid = [3, 1, 3, 0]

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
plt.bar(x + (4 * bar_width), flid, width=bar_width, label='FLID', color='magenta')

# Adding labels and title
plt.xlabel('Perception Categories')
plt.ylabel('Frequencies')
plt.title('PERCEPTION OF FUNCTIONALITY') # Title of the graph
plt.xticks(x, categories)
plt.legend()

# Show grid and plot
plt.grid(axis='y')
plt.tight_layout()
plt.show()