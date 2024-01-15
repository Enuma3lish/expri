import pandas as pd
def Read_csv():
    csv_file = '100000_Raw.csv'  # Replace with the path to your CSV file
# Read the CSV file into a DataFrame 
    data_frame = pd.read_csv(csv_file)
# Convert the DataFrame into a list of lists
    data_list = data_frame.values.tolist()
    return data_list

