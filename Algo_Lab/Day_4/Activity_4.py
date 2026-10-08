swaps = 0
pass_c = 0

ls = [75, 42, 89, 56, 91, 68, 33, 80]

print("Original Marks :",ls)

for a in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
            swaps += 1
        else:
            continue
        pass_c += 1
        print(f"Pass {pass_c} :",ls)

print("Highest Marks : ",max(ls))
print("Lowest Marks :",min(ls))
print("Sorted Marks :",ls)
