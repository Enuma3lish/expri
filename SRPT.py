import heapq

def srpt_scheduler(jobs):
    min_heap = []
    time = 0
    index = 0
    result = []
    
    while index < len(jobs) or min_heap:
        while index < len(jobs) and jobs[index][0] <= time:
            arrival_time, remaining_time = jobs[index]
            heapq.heappush(min_heap, (remaining_time, arrival_time, index))
            index += 1
        
        if min_heap:
            remaining_time, arrival_time, job_index = heapq.heappop(min_heap)
            result.append(job_index)
            remaining_time -= 1
            
            if remaining_time > 0:
                heapq.heappush(min_heap, (remaining_time, arrival_time, job_index))
            
            time += 1
        else:
            time += 1
    
    return result

def average_flow_time(jobs, execution_order):
    total_flow_time = 0
    completion_time = [0] * len(jobs)
    
    for index in execution_order:
        arrival_time, remaining_time = jobs[index]
        total_flow_time += (completion_time[index] - arrival_time)
        completion_time[index] += remaining_time
    
    return total_flow_time / len(jobs)
def Srpt(jobs):
# Example usage
    execution_order = srpt_scheduler(jobs)
    avg_flow_time = average_flow_time(jobs, execution_order)
    return avg_flow_time
