import random
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
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Original list:", arr)
    
    bubble_sort(arr)
    print("Sorted list:", arr)

main()