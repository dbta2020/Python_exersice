is_prime = int(input("Enter a number: "))
#Check prime number:
def check(is_prime):
    for i in range(2, is_prime):
        if is_prime % i == 0:
            return False
    return True
#checj if the number is prime:
if check(is_prime):
    print("The number is prime")
else:
    print("The number is not prime") 
