def Sjf(jobs):
    # Sort jobs by arrival time
    jobs.sort(key=lambda x: x[0])
    time = 0
    start_time = []
    job_sequence = []
    while jobs:
        # Filter jobs that have arrived
        available_jobs = [job for job in jobs if job[0] <= time]
        if not available_jobs:
            # If no jobs have arrived, increment time
            time += 1
            continue
        # Select job with smallest job_size
        shortest_job = min(available_jobs, key=lambda x: x[1])
        jobs.remove(shortest_job)
        job_sequence.append(shortest_job)

        # Calculate start time for each job
        start_time.append(time)
        time += shortest_job[1]

    # Calculate flow (turnaround) times
    flow_times = [start_time[i] + job_sequence[i][1] - job_sequence[i][0] for i in range(len(job_sequence))]
    average_flow_time = sum(flow_times) / len(flow_times)
    print(average_flow_time)
    return average_flow_time
