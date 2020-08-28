#ASHITA GOYAL (11) SEC - A1

def insertionSort(arr): 
   
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

l = list(map(int, input("ENTER THE LIST TO BE SORTED: ").split()))
insertionSort(l)
print("SORTED LIST: ", l)

#Time - Complexity : O(n^2)
