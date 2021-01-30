v = int(input())
p1_per_hour = int(input())
p2_per_hour = int(input())
h = float(input())

# Общо за всяка тръба
p1 = p1_per_hour * h
p2 = p2_per_hour * h

total_pipes = p1 + p2
percent_pipe1 = p1 / total_pipes * 100
percent_pipe2 = p2 / total_pipes * 100
percent_total_pipes = total_pipes / v * 100


if total_pipes > v:
    overflow = total_pipes - v
    print(f"For {h} hours the pool overflows with {overflow:.2f} liters.")
else:
    print(
        f"The pool is {percent_total_pipes:.2f}% full.Pipe 1: {percent_pipe1:.2f}%. Pipe 2: {percent_pipe2:.2f}%.")
