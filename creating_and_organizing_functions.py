def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) 
    
def main():
    n = int(input("Enter a non-negative integer: "))
    result = factorial(n)
    print(f"The factoiral of {n} is", result)

main()