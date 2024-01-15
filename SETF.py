import heapq

def setf_scheduler(jobs):
    time = 0
    result = []
    job_heap = []
    completion_times = {}  # Initialize a dictionary to store completion times

    while jobs or job_heap:
        # Add arrived jobs to the heap
        while jobs and jobs[0][0] <= time:
            arrival_time, remaining_time = jobs.pop(0)
            estimated_finish_time = time + remaining_time
            heapq.heappush(job_heap, (estimated_finish_time, arrival_time, len(result)))

        if job_heap:
            # Get the job with the shortest estimated time to finish
            estimated_finish_time, arrival_time, job_index = heapq.heappop(job_heap)
            result.append(job_index)

            # Calculate flow time for the selected job
            flow_time = time + 1 - arrival_time  # Adding 1 to account for the current time step
            completion_times[job_index] = flow_time  # Store completion time in the dictionary

            # Decrement remaining time for the selected job
            remaining_time -= 1

            if remaining_time > 0:
                # If the job still has remaining time, put it back into the heap
                estimated_finish_time = time + remaining_time
                heapq.heappush(job_heap, (estimated_finish_time, arrival_time, job_index))

            # Increment time
            time += 1
        else:
            # No available jobs, increment time
            time += 1

    return result, completion_times

# Function to calculate the average flow time
def average_flow_time(completion_times):
    return sum(completion_times.values()) / len(completion_times)

def Setf(jobs):
    execution_order, completion_times = setf_scheduler(jobs)
    avg_flow_time_value = average_flow_time(completion_times)
    print("Execution Order:", execution_order)
    print("Average Flow Time:", avg_flow_time_value)
    return avg_flow_time_value
