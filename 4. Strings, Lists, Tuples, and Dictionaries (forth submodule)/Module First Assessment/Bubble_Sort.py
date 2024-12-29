def bubble_sort(arr):
    n = len(arr)
    # Iterate over the array
    for i in range(n):
        # Perform comparisons and swaps for each pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are not in order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [42, 35, 12, 92, 65, 10, 23, 75, 81, 9]
    print("Original list:", arr)
    
    bubble_sort(arr)
    print("Sorted list:", arr)

main()