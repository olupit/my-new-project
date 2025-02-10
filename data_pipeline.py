import pandas as pd

# Load dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Process data: Fill missing values and normalise a column
def process_data(df):
    if df is not None:
        df.fillna(0, inplace=True)  # Fill missing values
        if 'value' in df.columns:
            df['normalised_value'] = df['value'] / df['value'].max()
        print("Data processed successfully!")
    return df

# Save processed data
def save_data(df, output_path):
    if df is not None:
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    input_file = "raw_data.csv"  # Assume this is in the repo
    output_file = "processed_data.csv"
    
    data = load_data(input_file)
    processed_data = process_data(data)
    save_data(processed_data, output_file)
