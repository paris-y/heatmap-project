import pandas as pd
import matplotlib.pyplot as plt

#Load data files
file_path = 'C:\\Users\\ysj04\\Downloads\\updated2.csv' #Replace with your own file path
df = pd.read_csv(file_path, header=None, skiprows=2, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
df.columns = ['Station', 'Class', 'Point', 'Length', 'Road Name', 'Beginning Description', 'End Description', 'AADT', '% Trucks']

#Create the histograms
plt.figure(figsize=(10, 5))
plt.hist(df['AADT'], bins=30, edgecolor='k', alpha=0.7)
plt.title('AADT Distribution')
plt.xlabel('AADT')
plt.ylabel('Frequency')
plt.savefig('aadt_distribution.png') #Save the AADT Distribution histogram
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df['% Trucks'], bins=30, edgecolor='k', alpha=0.7)
plt.title('% Trucks Distribution')
plt.xlabel('% Trucks')
plt.ylabel('Frequency')
plt.savefig('trucks_distribution.png') #Save the % Trucks Distribution histogram
plt.show()

#AADT Stats Summary
aadt_stats = df['AADT'].describe() 
aadt_min = df['AADT'].min() 
aadt_max = df['AADT'].max() 
aadt_mean = df['AADT'].mean() 
aadt_median = df['AADT'].median() 
aadt_std = df['AADT'].std()

print("Summary Statistics for AADT") 
print(aadt_stats) 

#% Trucks Stats Summary
trucks_stats = df['% Trucks'].describe() 
trucks_min = df['% Trucks'].min() 
trucks_max = df['% Trucks'].max() 
trucks_mean = df['% Trucks'].mean() 
trucks_median = df['% Trucks'].median() 
trucks_std = df['% Trucks'].std()

print("Summary Statistics for % Trucks") 
print(trucks_stats) 
