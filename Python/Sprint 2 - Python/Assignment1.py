# Assignment -
#  1. print prime nos,
#  2. even odd program,
#  3. create a list with duplicate values and make it unique

def prime(n):
        numbers = [i for i in range(2, n+1)]
        i = 0
        while i < len(numbers):
            if numbers[i] is not None:
                for j in range(i+numbers[i], len(numbers), numbers[i]):
                    numbers[j] = None
            i += 1

        return [j for j in numbers if j is not None]

def evenOdd(n):
    if n %2==0:
        print("The number is EVEN\n")
    else:
        print("The number is ODD\n")

def unique():
    l = ['asdf','asdf','asdf', 23, 23, 34, 1231, (21,12,'adf'), (21,12,'adf'), (21,12)]
    print(l)
    unique_l = list(set(l))
    print(unique_l,"\n")

n = int(input("\nEnter the number to get the prime numbers till that number: "))
lst = prime(n)
if len(lst) == 0:
    print("There are no prime numbers till", n)
else:
    print("The prime numbers in this range are:", lst, "\n")

def dict_travers():
    d = {}
    n = int(input("\nEnter the number of enteries you wanna put in this phone book: "))

    for i in range(n):
        key = input("Name of the person: ")
        value = input("Enter their mobile number: ")
        d[key] = value

    print("The phone now contains the following contacts:")
    for key , value in d.items():
        print(key, " : " ,value)


evenOdd(123)
unique()
dict_travers()