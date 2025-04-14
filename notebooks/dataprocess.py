import pandas as pd

def process_csv(input_file, output_file):
    """
    Reads a CSV file, processes it, and writes the processed data to a new file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the processed CSV file.
    """
    try:
        # Read the CSV file
        data = pd.read_csv(input_file)
        
        # Example processing: Drop rows with missing values
        processed_data = data.dropna()
        
        # Save the processed data to a new CSV file
        processed_data.to_csv(output_file, index=False)
        print(f"Processed data saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_csv = "input.csv"  # Replace with your input file path
    output_csv = "output.csv"  # Replace with your output file path
    process_csv(input_csv, output_csv)