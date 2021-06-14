from collections import deque

integers = deque(int(n) for n in input().split(', '))
needed_index = int(input())
needed_integer = integers[needed_index]
min_num = None
clock_cycles = 0

while True:
    if not integers:
        break
    min_num = min(integers)
    if min_num > needed_integer:
        break
    integers.remove(min_num)
    clock_cycles += min_num


print(clock_cycles)


########### SECOND HARDER WAY , bcs the exam is near, I panicked, and didnt solve it properly ####

jobs = deque([int(x) for x in input().split(', ')])
wanted_job_index = int(input())
wanted_job = jobs[wanted_job_index]
clock_cycles = 0

similar_jobs = [job for job in jobs if job == wanted_job]

while True:

    job_to_complete = min(jobs)
    current_job = jobs.popleft()
    if job_to_complete == current_job:
        clock_cycles += job_to_complete
        if job_to_complete == wanted_job:
            if len(similar_jobs) > 1:
                similar_jobs.pop()
            else:
                print(clock_cycles)
                break
    else:
        jobs.append(current_job)
