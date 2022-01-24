
def check_primality(num):
    primality = True
    i = 2
    upperlimit = num//i

    if(num == 2): #2 is prime
        return primality
    
    if(num == 1 or num == 0): #1 and 0 are not prime
        return False

    while(i<=upperlimit): #reduce the upper limit with each iteration for faster convergence
        if(num%i == 0):
            primality = False
            break
        else:
            i += 1
            upperlimit = num//i
    
    return primality

if __name__ == "__main__":

    print("\nPrinting the prime numbers from 1 to 1000...\n")
    for i in range(1000):
        if(check_primality(i)):
            print(i, end="\t")
        if(i%20==0):
            print()
    print("\n")
