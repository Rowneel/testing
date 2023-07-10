bt = [7, 6, 5]
temp = []
q = 2
n = len(bt)
t = 0
wt = [0]* n
tat = [0]*n
for i in range(n):
    temp.append(bt[i])
while(1):
    done = True
    for i in range(n):
        if (temp[i] > 0) :
            done = False 
            if (temp[i] > q) :
                t += q
                temp[i] -= q
            else:
                t  += temp[i]
                wt[i] = t - bt[i]
                temp[i] = 0
    if (done == True):
        break
for i in range(n):
        tat[i] = bt[i] + wt[i]
        print(" ", i + 1, "\t", bt[i], "\t", tat[i], "\t", wt[i])