def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
     for i in range(n):
         print(fibonacci_recursive(i), end=" ")

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_iterative(n)
