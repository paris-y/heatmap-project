import pandas as pd

file_path = 'C:\\Users\\ysj04\\Downloads\\updated1.csv' #Replace with your own file path
df = pd.read_csv(file_path)

#Copy column 11 data to column 10 for rows 1527 to 1540 (to align data properly for later use)
df.iloc[1526:1540, 9] = df.iloc[1526:1540, 10]

#Delete row 11 (since we already copied the data)
df = df.drop(columns=df.columns[10])

#Delete any rows with any missing values again
df.dropna(inplace=True)

#Delete any columns with any missing values again
df.dropna(axis=1, inplace=True)

#Show the cleaned DataFrame again
print("Cleaned Data:")
print(df)

#Save cleaned DataFrame as a new CSV file
updated_file_path = 'C:\\Users\\ysj04\\Downloads\\updated2.csv' #Replace with your own file path
df.to_csv(updated_file_path, index=False)
