
arr = [12, 35, 1, 10, 34, 1]


if len(arr) < 2:
    print("Array needs at least two elements.")
else:
   
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    
    for num in arr:
        
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    
    print("Second largest element:", second_largest)
    print("Second smallest element:", second_smallest)

