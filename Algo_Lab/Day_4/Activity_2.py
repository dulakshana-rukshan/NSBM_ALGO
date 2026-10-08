count = 0
pass_c = 0

ls = [45, 12, 78, 34, 23, 89, 10]

for a in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j] < ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
            count += 1
        else:
            continue
        pass_c += 1
        print(f"Pass {pass_c} :",ls)


print("Original Array :",ls)
print("Number of swaps:" ,count)