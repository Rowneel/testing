#tuple is defined as (processNo,BT,Priority)
process = [(1,7,3),(2,6,1),(3,5,2)]
n = len(process)
p = [tup[0] for tup in process]
bt = [tup[1] for tup in process]
wt = [sum(bt[:i]) for i in range(n)]
tat = [wt[i] + bt[i] for i in range(n)]
print(f"process\tBT\tTAT\tWT")
for i in range(n):
    print(f"{p[i]}\t{bt[i]}\t{tat[i]}\t{wt[i]}")

process.sort(key=lambda x:x[2])
p = [tup[0] for tup in process]
pr = [tup[2] for tup in process]
bt = [tup[1] for tup in process]
wt = [sum(bt[:i]) for i in range(n)]
tat = [wt[i] + bt[i] for i in range(n)]
print(f"process\tPrio\tBT\tTAT\tWT")
for i in range(n):
    print(f"{p[i]}\t{pr[i]}\t{bt[i]}\t{tat[i]}\t{wt[i]}")

process.sort(key=lambda x:x[1])
p = [tup[0] for tup in process]
bt = [tup[1] for tup in process]
wt = [sum(bt[:i]) for i in range(n)]
tat = [wt[i] + bt[i] for i in range(n)]
print(f"process\tBT\tTAT\tWT")
for i in range(n):
    print(f"{p[i]}\t{bt[i]}\t{tat[i]}\t{wt[i]}")
    

