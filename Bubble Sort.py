#ASHITA GOYAL (11) SEC - A1

def bubbleSort(arr): 
    n = len(arr) 
   
    for i in range(n-1):  
        for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

l = list(map(int, input("ENTER THE LIST TO BE SORTED: ").split()))
bubbleSort(l)
print("SORTED LIST: ", l)

#Time - Complexity : O(n^2)
