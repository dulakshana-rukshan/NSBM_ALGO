ls = []
pass_c = 0
swaps = 0

for i in range(5):
    num =  int(input(f"Enter Number {i+1}:"))

    ls.append(num)

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
print("Number Of Swaps :",swaps)
print("Largest Number :",max(ls))
print("Smallest Number :",min(ls))




