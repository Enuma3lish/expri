import queue
num_queues = 3
queues = [queue.Queue() for _ in range(num_queues)]

# Simulate MLFQ scheduling and calculate flow time

# generate_job_size()
def Mlfq(job_list):
    floor_size = 2
    current_time = 0
    total_flow_time = 0
    job_count = 0
    job_flow=[]
    while job_list or any(not q.empty() for q in queues):
    # Move jobs from job_list to appropriate queue based on arrival time
        while job_list and job_list[0][0] <= current_time:
            job = job_list.pop(0)
            if job[1] <= floor_size:
                queues[0].put(job)
            elif job[1] <= 3*floor_size:
                queues[1].put(job)
            else:
                queues[2].put(job)

    # Process queues with different priorities
        for i, q in enumerate(queues):
            if not q.empty():
                job = q.get()
                #print(f"Processing job with priority {i+1}: Arrival Time={job['arrival_time']}, Job Size={job['job_size']}")
                flow_time = current_time - job[0]
                job_flow.append(flow_time)
                total_flow_time += flow_time
                job_count += 1
                current_time += job[1]
                break  # Move to the next queue after processing one job
        current_time += 1  # Time quantum or context switch time

# Calculate average flow time
    average_flow_time = total_flow_time / job_count if job_count > 0 else 0
# Print results
    #print(f"Total Flow Time: {total_flow_time}")
    #print(f"MLFQ Average Flow Time: {average_flow_time}")
    return average_flow_time
