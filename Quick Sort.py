#ASHITA GOYAL (11) SEC - A1

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
 
    for j in range(low, high):
 
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

l = list(map(int, input("ENTER THE LIST TO BE SORTED: ").split()))
quickSort(l, 0, len(l) - 1)
print("SORTED LIST: ", l)

#Time - Complexity :
  #Worst Case : O(n^2)
  #Average Case : O(nlogn)
  #Best Case : O(nlogn)
