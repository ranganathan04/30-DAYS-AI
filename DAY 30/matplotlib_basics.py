import matplotlib.pyplot as plt
import pandas as pd

# Read sample data
df = pd.read_csv('sample_data.csv')

# 1. Line Chart
plt.figure(figsize=(6, 4))
plt.plot(df['Name'], df['Score'], marker='o', color='blue')
plt.title('Line Chart: Scores by Student')
plt.xlabel('Student')
plt.ylabel('Score')
plt.grid(True)
plt.tight_layout()
plt.savefig('line_chart.png')
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Name'], df['Score'], color='orange')
plt.title('Bar Chart: Scores')
plt.xlabel('Student')
plt.ylabel('Score')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# 3. Pie Chart
plt.figure(figsize=(5, 5))
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%')
plt.title('Pie Chart: Score Distribution')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()
