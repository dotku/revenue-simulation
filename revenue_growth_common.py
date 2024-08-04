import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the simulation
num_months = 24
initial_revenue = 10000  # Initial monthly revenue
very_high_growth_rate = 0.30  # 30% monthly growth for the first 6 months
moderate_growth_rate = 0.15  # 15% monthly growth for the next 12 months
stabilized_growth_rate = 0.05  # 5% monthly growth for the remaining period

# Generate the revenue data
months = np.arange(1, num_months + 1)
revenue = np.zeros(num_months)

# Calculate revenue for each month
for month in range(num_months):
    if month == 0:
        revenue[month] = initial_revenue
    elif month < 6:
        revenue[month] = revenue[month - 1] * (1 + very_high_growth_rate)
    elif month < 18:
        revenue[month] = revenue[month - 1] * (1 + moderate_growth_rate)
    else:
        revenue[month] = revenue[month - 1] * (1 + stabilized_growth_rate)

# Create a DataFrame for better visualization and manipulation
revenue_data = pd.DataFrame({
    'Month': months,
    'Revenue': revenue
})

# Plot the revenue data
plt.figure(figsize=(10, 6))
plt.plot(revenue_data['Month'], revenue_data['Revenue'], marker='o', linestyle='-', color='b')
plt.title('Tech Startup Monthly Revenue Simulation')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.show()

# Display the DataFrame
print(revenue_data)