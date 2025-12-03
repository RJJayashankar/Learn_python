def main():
    symbol = input("enter a symbol: ")
    no_of_iter = int(input("enter the number of times it should print"))
    #print_row(no_of_iter,symbol)
    #print_col(no_of_iter,symbol)
    #print_square(no_of_iter,symbol)
    #print_inverted_square(no_of_iter,symbol)
    #print_triangle(no_of_iter,symbol)
    print_pyramid(no_of_iter,symbol)

def print_row(n,symbol):
    for _ in range(n):
        print(symbol)
    print()

def print_col(n,symbol):
    for _ in range(n):
        print(symbol,end="")
    print()
    print()


def print_square(n,symbol):
    for i in range(n):
        for j in range(n):
            print(symbol,end="")
        print()

def print_inverted_square(n,symbol):
    for i in range(n):
        for j in range(n-i):
            print(symbol,end="")
        print()
        print()

def print_triangle(n,symbol):
    for i in range(n):
        for j in range(i+1):
            print(symbol,end="")
        print()

def print_pyramid(n,symbol):
    for i in range(n):
        print(symbol)
        for j in range(i)

        
        
main()