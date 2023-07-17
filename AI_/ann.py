def step(val):
    if val >= 0.5:
        return 1
    else:
        return 0

x1 , x2 = [0, 0, 1, 1], [0, 1, 0, 1]
y = [0, 1, 1, 1]
w1,w2 = 0.1, 0.5
alpha = 0.1
flag = True
epoch = 0

for i in range(4):
    print(f"{x1[i]}\t{x2[i]}\t{ y[i]}")

while (flag):
    flag = False
    epoch +=1
    print(f"epoch: {epoch}")
    for i in range(4):
        print(f"w1: {w1} \tw2: {w2}")
        ya = step(x1[i] * w1 + x2[i] * w2)
        # error calc
        error = y[i] - ya
        if error != 0:
            flag = True
            w1 = w1 + error * alpha * x1[i]
            w2 = w2 + error * alpha * x2[i]
print("Testing: ")
for i in range(4):
    print(f"{x1[i]}\t{x2[i]}\t{step(x1[i] * w1 + x2[i] * w2)}")