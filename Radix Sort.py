#ASHITA GOYAL (11) SEC - A1

def countingSort(arr, exp1): 
   
    n = len(arr) 
    
    output = [0] * (n) 
   
    count = [0] * (10) 
   
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
    
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
def radixSort(arr):
 
    max1 = max(arr)
 
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

l = list(map(int, input("ENTER THE LIST TO BE SORTED: ").split()))
radixSort(l)
print("SORTED LIST: ", l)

#Time - Complexity : O((n+b) * logb(k)), where b is the base for representing numbers, d is the digits in input integers, k is the maximum possible value, n is the number of inputs.
