def main():
    n = int(input("enter the number of meows:"))
    meow(validate_if_no_positive(n))


def validate_if_no_positive(n):
    while True:
        if n > 0:
            break
        else:
            return n
        

def meow(n):
    for i in range(n):
        print("meow")

main()
