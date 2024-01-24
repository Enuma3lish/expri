def fcfs_scheduler(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time

def Fcfs(jobs):
    # Example usage with a list of processes where each process is represented as (arrival_time, burst_time)
    waiting_time, turnaround_time = fcfs_scheduler(jobs)

    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(turnaround_time)
    print("average flow time",average_turnaround_time)
    return average_turnaround_time
