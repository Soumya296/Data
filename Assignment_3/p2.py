def bubbleSort(arr):
    n = len(arr)
    count = 1
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.

        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            print("Pass number: %d"%count)
            count += 1
            print("Current sorted array: ",arr,end="\n\n")
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":

    size = int(input("Enter the number of elements in the array... "))
    arr = []
    print("Keep entering the elements...\n")
    for i in range(size):
        element = int(input())
        arr.append(element)
    
    print("\nPrinting the unsorted array...")
    print(arr)

    bubbleSort(arr)
    print("Printing the sorted array...")
    print(arr, end="\n\n")