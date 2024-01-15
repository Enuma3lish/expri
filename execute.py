import multiprocessing
import Read_csv
import MLFQ,RR,SJF,SRPT
#Arrival_rate=[0.05,0.04545,0.0416,0.0385,0.036,0.033,0.3123,0.029,0.028,0.026,0.025]
bp_parameter=[{"L":16.772,"H":pow(2,6)},{"L":7.918,"H":pow(2,9)},{"L":5.649,"H":pow(2,12)},{"L":4.073,"H":pow(2,18)}]
def process_scheduler(func, data):
    return func(data)
def execute(Arrival_rate,bp):
    job_list = Read_csv.Read_csv()
    rr_list = job_list.copy()
    sjf_list = job_list.copy()
    srpt_list = job_list.copy()
    pool = multiprocessing.Pool(processes=4)
    mlfq = 0
    mlfq_arr = []
    rr = 0
    rr_arr=[]
    sjf = 0
    sjf_arr = []
    srpt = 0
    result = {}
    for _ in range(10):
        num_processes = 4
        with multiprocessing.Pool(processes=num_processes) as pool:
        # Use starmap to run the functions in parallel
            results = pool.starmap(
                process_scheduler,
                [(MLFQ.Mlfq, job_list), (RR.Rr, rr_list), (SRPT.Srpt, srpt_list), (SJF.Sjf, sjf_list)]
            )
            mlfq,rr,srpt,sjf = results
            sjf_result = sjf/srpt 
            rr_result = rr/srpt
            mlfq_result = mlfq/srpt
            result.update({"arrival_rate":Arrival_rate,"bp_parameter":bp,"SJF/SRPT":sjf_result,"RR/SRPT":rr_result,"MLFQ/SRPT":mlfq_result})
    pool.close()
    pool.join()
    return result
        
    