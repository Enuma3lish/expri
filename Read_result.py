import pandas as pd
import matplotlib.pyplot as plt
import ast
# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('100000_data.csv')
x =df[df['bp_parameter']=="{'L': 16.772, 'H': 64}"]
x_arrival = x['arrival_rate'].to_list()
print(x)
x_label = [0.05, 0.04545, 0.0416, 0.0385, 0.036, 0.033, 0.03123, 0.029, 0.028, 0.026, 0.025]
y_sjf = x['SJF/SRPT'].to_list()
print(y_sjf)
y_rr = x['RR/SRPT'].to_list()
y_mlfq =x['MLFQ/SRPT'].tolist()
y_setf = x['SETF/SRPT'].tolist()
plt.figure(figsize=(20,10))  # Adjust the figure size as needed
plt.plot(x_label,y_sjf, label='SJF/SRPT')
# plt.plot(x_arrival,y_rr, label='RR/SRPT')
# plt.plot(x_arrival,y_mlfq, label='MLFQ/SRPT')
# plt.plot(x_arrival,y_setf, label='SETF/SRPT')
# Add labels and legend
plt.xlabel('arrival_rate')
plt.ylabel('Compare')
plt.legend()

# # Optionally, customize the title and save the figure
plt.title(0.05)
# # Show the plot
plt.savefig("result.jpg")

    