#ASHITA GOYAL (11) SEC - A1

def selectionSort(arr):

    for i in range(len(arr)): 
    
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

l = list(map(int, input("ENTER THE LIST TO BE SORTED: ").split()))
selectionSort(l)
print("SORTED LIST: ", l)

#Time - Complexity : O(n^2)
