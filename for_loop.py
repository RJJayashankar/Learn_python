def main():
    n = int(input("enter the number of times the cat should meow"))
    print_meow(n)


def print_meow(n):
    for i in range(n):
        print("meow")

main()