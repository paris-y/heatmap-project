import pandas as pd

file_path = 'C:\\Users\\ysj04\\Downloads\\localrdreport.csv' #Replace this with your own file path
df = pd.read_csv(file_path, header=None)

#Remove any rows that are completely empty
df.dropna(how='all', inplace=True)

#Remove any columns that are completely empty
df.dropna(axis=1, how='all', inplace=True)

#Remove the first row (unnecessary after viewing data)
df = df.iloc[1:].reset_index(drop=True)

#If column only has a header and no other data, then remove it
columns_to_drop = [col for col in df.columns if df[col].isna().all()] 
df.drop(columns=columns_to_drop, inplace=True)

#Reset the index of the columns 
df.columns = range(df.shape[1])

#Show the cleaned DataFrame
print("Cleaned Data:")
print(df)

#Save cleaned DataFrame as a new CSV file
cleaned_v1 = 'C:\\Users\\ysj04\\Downloads\\updated1.csv'
df.to_csv(cleaned_v1, index=False)
