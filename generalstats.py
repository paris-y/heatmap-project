import pandas as pd

#Load data from CSV and skip two rows
file_path = 'C:\\Users\\ysj04\\Downloads\\updated2.csv' #Replace with your file path
df = pd.read_csv(file_path, header=None, skiprows=2)

#Select columns by index and rename it
df = df.iloc[:, [7, 8]] 
df.columns = ['AADT', '% Trucks']

#Calculate general stats for aadt and % truck
aadt_stats = {
    'min': df['AADT'].min(), 
    'max': df['AADT'].max(),
    'mean': df['AADT'].mean(),
    'median': df['AADT'].median(),
    'std_dev': df['AADT'].std()
}

trucks_stats = {
    'min': df['% Trucks'].min(),
    'max': df['% Trucks'].max(),
    'mean': df['% Trucks'].mean(),
    'median': df['% Trucks'].median(),
    'std_dev': df['% Trucks'].std()
}

print('AADT Statistics:', aadt_stats)
print('Trucks Percentage Statistics:', trucks_stats)