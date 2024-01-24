import heapq

def Setf(jobs):
    total_time = 0  # Total time elapsed
    completion_time = {}  # Dictionary to store completion time for each job
    remaining_service = {}  # Dictionary to store remaining service time for each job

    # Initialize remaining service times for each job
    for arrival_time, job_size in jobs:
        remaining_service[(arrival_time, job_size)] = job_size

    event_queue = []  # Priority queue for events
    heapq.heapify(event_queue)

    current_time = 0  # Current time

    while jobs or event_queue:
        # Check if any jobs have arrived
        while jobs and jobs[0][0] <= current_time:
            arrival_time, job_size = jobs.pop(0)
            heapq.heappush(event_queue, (arrival_time, job_size))

        if not event_queue:
            # No jobs in the queue, wait for the next job to arrive
            current_time = jobs[0][0]
        else:
            # Choose the job with the shortest remaining service time
            arrival_time, job_size = heapq.heappop(event_queue)
            remaining_time = min(remaining_service[(arrival_time, job_size)], jobs[0][0] - current_time) if jobs else remaining_service[(arrival_time, job_size)]
            current_time += remaining_time
            remaining_service[(arrival_time, job_size)] -= remaining_time

            if remaining_service[(arrival_time, job_size)] == 0:
                completion_time[(arrival_time, job_size)] = current_time

    # Calculate flow times and average flow time
    flow_times = [completion_time[(arrival_time, job_size)] - arrival_time for arrival_time, job_size in completion_time]
    average_flow_time = sum(flow_times) / len(flow_times)
    
    return average_flow_time

