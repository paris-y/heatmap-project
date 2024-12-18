import pandas as pd

#Load data from CSV, skip first two rows and last column
file_path = 'C:\\Users\\ysj04\\Downloads\\updated2.csv' #Replace with your own file path
df = pd.read_csv(file_path, header=None, skiprows=2, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])

#Rename columns
df.columns = ['Station', 'Class', 'Point', 'Length', 'Road Name', 'Beginning Description', 'End Description', 'AADT', '% Trucks']

#Get row with the minimum AADT
min_aadt_row = df.loc[df['AADT'].idxmin()]

#Get row with the maximum AADT
max_aadt_row = df.loc[df['AADT'].idxmax()]

#Get row with the minimum % trucks
min_trucks_row = df.loc[df['% Trucks'].idxmin()]

#Get row with the maximum % trucks
max_trucks_row = df.loc[df['% Trucks'].idxmax()]

#Print those rows accordingly
print("Row with Minimum AADT:\n", min_aadt_row)
print("\nRow with Maximum AADT:\n", max_aadt_row)
print("\nRow with Minimum % Trucks:\n", min_trucks_row)
print("\nRow with Maximum % Trucks:\n", max_trucks_row)

#Get top 10 rows with the highest AADT and top 10 rows with highest % trucks
top_10_aadt = df.nlargest(10, 'AADT') 
top_10_trucks = df.nlargest(10, '% Trucks') 

#Show stats of the top 10 rows 
print("\nTop 10 Rows by AADT:\n", top_10_aadt) 
print("\nTop 10 Rows by % Trucks:\n", top_10_trucks)
