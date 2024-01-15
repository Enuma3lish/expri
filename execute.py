import multiprocessing
import Read_csv
import MLFQ,RR,SJF,SRPT,SETF
#Arrival_rate=[0.05,0.04545,0.0416,0.0385,0.036,0.033,0.3123,0.029,0.028,0.026,0.025]
def process_scheduler(func, data):
    return func(data)
result =[]
def execute(Arrival_rate,bp_parameter):
    for i in bp_parameter:
        job_list = Read_csv.Read_csv(str(i["L"])+".csv")
        rr_list = job_list.copy()
        sjf_list = job_list.copy()
        srpt_list = job_list.copy()
        setf_list = job_list.copy()
        mlfq = 0
        rr = 0
        sjf = 0
        srpt = 0
        setf = 0
        num_processes = 5
        with multiprocessing.Pool(processes=num_processes) as pool:
        # Use starmap to run the functions in parallel
            results = pool.starmap(
                process_scheduler,
                    [(MLFQ.Mlfq, job_list), (RR.Rr, rr_list), (SRPT.Srpt, srpt_list), (SJF.Sjf, sjf_list),(SETF.Setf,setf_list)]
                )
            mlfq,rr,srpt,sjf,setf = results
            
            sjf_result = sjf/srpt 
            rr_result = rr/srpt
            mlfq_result = mlfq/srpt
            setf_result = setf/srpt
            result.append({
                "arrival_rate":Arrival_rate,
                "bp_parameter":i,
                "SJF/SRPT":sjf_result,
                "RR/SRPT":rr_result,
                "MLFQ/SRPT":mlfq_result,
                "SETF/SRPT":setf_result
            })
        pool.close()
        pool.join()
    return result
        
    