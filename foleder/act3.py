def rec(n):
    if n == 0:
        return 0
    else:
        remainder = n % 10  
        quotient = n // 10 
        
       
        print(f"Number: {n}, Quotient: {quotient}, Remainder: {remainder}")
        
        return remainder + rec(quotient)  

n = int(input("Enter a number: "))
print("Sum of remainders:", rec(n))
