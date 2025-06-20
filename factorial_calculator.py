def factorial(n): 
    if n == 0: 
        return 1 
    else:   
        return n * factorial(n-1)   
    
def get_factorial_input(): 
    while True:
        try:    
            num = int(input("Enter a non-negative integer for factorial computation:"))
            if num >=0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")            

number = get_factorial_input() 
print(f"The factorial of {number} is {factorial(number)}")