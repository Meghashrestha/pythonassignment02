# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.
def is_prime(x):

    num= int(input("Enter a number: "))
    if (num > 1):
        divisor = 2
        for i in range(divisor,num):
            if (num % i) == 0:
                return False
    else:
        return False
    return True

print ("Is PRIME: ",is_prime('num'))