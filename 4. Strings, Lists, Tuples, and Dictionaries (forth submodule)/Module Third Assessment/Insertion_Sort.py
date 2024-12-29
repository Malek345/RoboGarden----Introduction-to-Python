import random

def insertion_sort(arr):
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def main():

    arr = [random.randint(0, 100) for _ in range(10)] 
    print("Original list:", arr)

    insertion_sort(arr)
    print("Sorted list:", arr)

main()
