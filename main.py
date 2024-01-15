#create dataset 
import Job_init
import matplotlib.pyplot as plt
import Write_csv
import execute
num_jobs = 100
results =[]
result = []
def main():
    Job_init.Save_file(num_jobs)
    h1 = pow(2,6)
    h2 = pow(2,9)
    h3 = pow(2,12)
    h4 = pow(2,18)
    print(h1)
    print(type(h2))
    Arrival_rate=[0.05,0.04545,0.0416,0.0385,0.036,0.033,0.3123,0.029,0.028,0.026,0.025]
    bp_parameter=[{"L":16.772,"H":h1},{"L":7.918,"H":h2},{"L":5.649,"H":h3},{"L":4.073,"H":h4}]
    for i in Arrival_rate:
        for j in bp_parameter:
            results = execute.execute(i,j) 
            result.append(results)
    Write_csv.write("/home/melowu/Work/expri/100000_data.csv",result)
if __name__ == "__main__":
    main()


    