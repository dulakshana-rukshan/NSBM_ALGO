comparisons = 0
swaps = 0
pass_c = 0

ls = [25, 17, 31, 13, 2, 45, 8]

print("Original Array :",ls)

for a in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
            swaps += 1
        else:
            continue
        pass_c += 1
        print(f"Pass {pass_c} :",ls)


print("Sorted Array :",ls)
print("Number of swaps:" ,swaps)