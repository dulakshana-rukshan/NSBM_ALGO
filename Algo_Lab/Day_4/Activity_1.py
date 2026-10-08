ls =[]
count = 0

for i in range(8):
    num =  int(input(f"Enter Number {i+1}:"))

    ls.append(num)

print(ls)
for a in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
            count += 1
        else:
            continue
        print(ls)

print("Number of swaps:" ,count)