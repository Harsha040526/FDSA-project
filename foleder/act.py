
arr = [12, 35, 1, 10, 34, 1]


largest = arr[0]
smallest = arr[0]


for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num


print("Largest element:", largest)
print("Smallest element:", smallest)



