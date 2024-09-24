import matplotlib.pyplot as plt

# Data
labels = ['FEES', 'HOUSES', 'LIVESTOCK', 'FOOD', 'EQUIP', 'P.-CASH', 'CLOTHES', 'EMPLOY']
values = [45, 27, 22, 56, 16, 4, 3, 6]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar plot
ax.bar(labels, values)

# Set the title and axis labels
ax.set_title('Benefits from Irrigation Farming')
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()

# Data
labels = ['FEES', 'HOUSES', 'LIVESTOCK', 'FOOD', 'EQUIP', 'P.-CASH', 'CLOTHES', 'EMPLOY']
values = [45, 27, 22, 56, 16, 4, 3, 6]

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Benefits from Irrigation Farming')

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()