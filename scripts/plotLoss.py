import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = os.path.join("simulations", "2024-04-19 0202", 'data.csv')

# Read the CSV file
df = pd.read_csv(FILE_PATH)
# Create cumulative bar plot
plt.figure(figsize=(10, 6))
plt.plot(df["step_num"])
plt.xlabel('Episode')
plt.ylabel('Time (seconds)')
plt.title('Graphique montrant l\'évolution du temps d\'exécution pour le jeu catcher')

# Show plot
plt.show()
