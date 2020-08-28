#ASHITA GOYAL (11) SEC - A1

def countSort(a, k): 
   
    c = []
    b = []
    for g in range(len(a)):
       b.append(0);
    for i in range(0, k + 1):
        c.append(0);
    for j in range(0, len(a)):
        c[a[j]] += 1
    for k in range(1, k + 1):
        c[k] = c[k] + c[k - 1]
    for l in range(len(a) - 1, -1, -1):
        b[c[a[l]] - 1] = a[l]
        c[a[l]] -= 1
    return (b)

a = list(map(int, input("ENTER THE ARRAY TO BE SORTED: ").split()))
print("THE SORTED ARRAY: ", countSort(a, max(a)))


#Time - Complexity : O(n)
