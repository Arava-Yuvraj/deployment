import pandas as pd

# Read the CSV file
input_file = "input.csv"
df = pd.read_csv(input_file)

# Process the data (example: filter rows where 'age' > 30)
filtered_df = df[df['age'] > 30]

# Write the processed data to a new CSV file
output_file = "output.csv"
filtered_df.to_csv(output_file, index=False)

print(f"Processed data has been written to {output_file}")
