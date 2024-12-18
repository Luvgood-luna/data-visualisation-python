import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read the CSV file
data = pd.read_csv('output.csv')

# column1 = data.columns[0].split(" ")
column_1 = data["IP-Address"]
column_2 = data["Success"] 
column_3 = data["Failed"]

#We have all the columns, 
# Now let's plot the graph
# Plot configuration
x = np.arange(len(column_1))  # x positions for groups
width = 0.4

fig, ax = plt.subplots(figsize=(18, 8))
ax.bar(x - width/2, column_2, width, label = 'Sucess' , color = 'green')
ax.bar(x + width/2, column_3, width, label = 'Failed' , color = 'red')

# Add labels titles and legends
ax.set_xlabel('IP Address')
ax.set_ylabel('Count')
ax.set_title('Success Vs Failed Attempts by IP Address')

ax.set_xticks(x)
ax.set_xticklabels(column_1, rotation=45)  # Rotate for readability

ax.legend()

plt.tight_layout()
plt.show()