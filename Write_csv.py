import csv
import pandas as pd
def Write_raw(filename,source):
    pd.DataFrame(source).to_csv(filename, index=None)
def Write(filename,source):
    pd.DataFrame(source).to_csv(filename, index=None)
# Flatten the nested dictionary
#     flattened_data = []
#     for item in source:
#         flattened_item = {
#             'arrival_rate': item['arrival_rate'],
#             'L': item['bp_parameter']['L'],
#             'H': item['bp_parameter']['H'],
#             'SJF/SRPT': item['SJF/SRPT'],
#             'RR/SRPT': item['RR/SRPT'],
#             'MLFQ/SRPT': item['MLFQ/SRPT'],
#             'SETF/SRPT': item['SETF/SRPT']
#         }
#         flattened_data.append(flattened_item)

# # Specify the header for the CSV file
#     header = ['arrival_rate', 'L', 'H', 'SJF/SRPT', 'RR/SRPT', 'MLFQ/SRPT', 'SETF/SRPT']

# # Specify the CSV file path
#     csv_file = filename

# # Write the data to the CSV file
#     with open(csv_file, mode='w', newline='') as file:
#          writer = csv.DictWriter(file, fieldnames=header)
    
#     # Write the header
#          writer.writeheader()
    
#     # Write the data
#          writer.writerows(flattened_data)

#          print(f'Data written to {csv_file}')
