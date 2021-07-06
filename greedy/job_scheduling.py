def jobScheduling(Jobs, n):
    count = 0
    profit = 0
    
    max_deadline = 0
    for job in Jobs:
        max_deadline = max(max_deadline, job.deadline)

    Jobs.sort(key=lambda job: job.profit, reverse=True)
        
    timeline = [-1]*max_deadline
    for job in Jobs:
        pos = job.deadline - 1
        while timeline[pos] != -1 and pos > 0:
            pos -= 1
        if timeline[pos] == -1:
            timeline[pos] = 1
            count += 1
            profit += job.profit
        else:
            pass
    
    return count, profit

class Job:
    def __init__(self, deadline, profit) -> None:
        self.deadline = deadline
        self.profit = profit

if __name__ == '__main__':
    n = int(input().strip())
    jobs = []
    for _ in range(n):
        deadline, profit = map(int, input().strip().split(" "))
        jobs.append(Job(deadline, profit))
    count, profit = jobScheduling(jobs, n)
    print("{} {}".format(count, profit))