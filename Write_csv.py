import csv
def write(filename,data_from):
    with open(filename,"w",newline='') as csvfile:
         print(data_from[0])
         fieldname = data_from[0].keys()
         writer = csv.DictWriter(csvfile,fieldname)
         writer.writeheader()
         for i in data_from:
             writer.writerow(i)