import numpy as np
def Mlfq(jobs):
  # Define the number of queues and quantum sizes
  num_queues = 100
  quantum_sizes = [pow(2,i)*max(1,2-np.random.exponential(scale=12, size=1)) for i in range(num_queues)]

  # Initialize variables
  time = 0
  total_flow_time = 0
  queues = [[] for _ in range(num_queues)]

  # Sort jobs by arrival time
  jobs.sort(key=lambda job: job[0])

  # Loop through jobs
  for arrival_time, job_size in jobs:
    # Wait until the job can be processed
    time = max(time, arrival_time)

    # Find the appropriate queue for the job
    queue_index = 0
    while queue_index < num_queues - 1 and job_size > quantum_sizes[queue_index]:
      queue_index += 1

    # Add the job to the queue
    queues[queue_index].append((arrival_time, job_size, 0))

    # Process jobs in each queue
    for i in range(num_queues - 1, -1, -1):
      while queues[i]:
        job_arrival_time, job_size, remaining_time = queues[i].pop(0)

        # Update remaining time and flow time
        remaining_time = min(remaining_time + 1, quantum_sizes[i])
        flow_time = time - job_arrival_time

        # Check if job is finished
        if remaining_time == job_size:
          total_flow_time += flow_time
        else:
          queues[i].append((job_arrival_time, job_size, remaining_time))
          break

    # Update time
    time += 1

  # Calculate average flow time
  avg_flow_time = total_flow_time / len(jobs)

  return avg_flow_time
