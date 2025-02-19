def get_remainder_and_quotient(numbers):
    remainders = []
    quotients = []
    
    for num in numbers:
        remainder = num % 10 
        quotient = num // 10  
        remainders.append(remainder)
        quotients.append(quotient)
    
    return remainders, quotients


n = int(input("Enter the number of terms: "))


numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


remainders, quotients = get_remainder_and_quotient(numbers)


print("Remainders:", remainders)
print("Quotients:", quotients)
