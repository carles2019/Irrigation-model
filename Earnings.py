import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Create a DataFrame with the provided data
data = {
    'Plot Size': [0.1, 0.16, 0.2, 0.25, 0.3, 0.35, 0.45, 0.5, 0.8, 0.9,
                  1, 1.3, 1.5, 1.7, 2, 2.5, 3, 4, 5],
    'Average Earnings': [517, 130, 570, 150, 408, 100, 1200,
                        900, 930, 460, 1350, 2500,
                        1710, 400, 2760, 3500,
                        450, 2050, 2400]
}

df = pd.DataFrame(data)

# Create a smooth line graph using cubic spline interpolation
x_new = np.linspace(df['Plot Size'].min(), df['Plot Size'].max(), 300) # Create new x values for smoothness
spline = make_interp_spline(df['Plot Size'], df['Average Earnings'], k=3) # Cubic spline interpolation
y_new = spline(x_new) # Calculate new y values

# Create the plot
plt.figure(figsize=(10,6))
plt.plot(x_new, y_new, color='blue') # Wave-like line without points
plt.title('Plot Size vs Average Earnings') # Title of the graph
plt.xlabel('Plot Size') # X-axis label
plt.ylabel('Average Earnings') # Y-axis label
plt.grid(True) # Show grid
plt.show() # Display the plot