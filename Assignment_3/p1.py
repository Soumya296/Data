
from utils import check_primality

if __name__ == "__main__":

    print("\nPrinting the prime numbers from 1 to 1000...\n")
    for i in range(1000):
        if(check_primality(i)):
            print(i, end="\t")
        if(i%20==0):
            print()
    print("\n")
