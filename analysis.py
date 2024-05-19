import pandas as pd

df = pd.read_csv('/data/Border_Crossing_Entry_Data.csv')

ca = df[df['Border'] == 'US-Canada Border']
us_mexico_border = df[df['Border'] == 'US-Mexico Border']

# Write the split data into two separate CSV files
ca.to_csv('us_canada_border.csv', index=False)
us_mexico_border.to_csv('us_mexico_border.csv', index=False)

print("Data has been split and saved to CSV files successfully.")