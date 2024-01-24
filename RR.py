import queue
import numpy as np
def round_robin_scheduling(job_list):
    time_quantum = 1
    ready_queue = queue.Queue()
    current_time = 0
    completed_jobs = []
    while job_list or not ready_queue.empty():
        # Add jobs to the ready queue that have arrived by the current time
        while job_list and job_list[0][0] <= current_time:
            ready_queue.put(job_list.pop(0))
        if not ready_queue.empty():
            current_job = ready_queue.get()
            if abs(current_job[1]) <= time_quantum:
                # Job finishes within time quantum
                current_time += current_job[1]
                completed_jobs.append({
                    'arrival_time': current_job[0],
                    'job_size': current_job[1],
                    'finish_time': current_time
                })
            else:
                # Job does not finish within time quantum, push it back to the queue
                current_time += time_quantum
                current_job[1] -= time_quantum
                ready_queue.put(current_job)
        else:
            # No jobs in the ready queue, increment time
            current_time += 1

    return completed_jobs

# Function to calculate flow time for a list of completed jobs
def calculate_flow_time(completed_jobs):
    job_flow=[]
    total_flow_time = 0
    for job in completed_jobs:
        job_flow.append(job['finish_time'] - job['arrival_time'])
        total_flow_time += (job['finish_time'] - job['arrival_time'])
    return total_flow_time/len(completed_jobs),job_flow

# Function to calculate average flow time
# def calculate_average_flow_time(completed_jobs):
#     total_flow_time= calculate_flow_time(completed_jobs)
#     return total_flow_time / len(completed_jobs)
def Rr(joblist=[]):
# Usage example
    #time_quantum = 100  # Time quantum for Round-Robin scheduling
    job_list = joblist.copy()
    completed_jobs = round_robin_scheduling(job_list)
    avg_flow_time,job_flow = calculate_flow_time(completed_jobs)
    #print("Flow times for completed jobs:", [job['finish_time'] - job['arrival_time'] for job in completed_jobs])
    print("RR Average flow time:", avg_flow_time)
    return avg_flow_time
