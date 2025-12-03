def main():
    students = ["Alice", "Bob", "Charlie", "David"]
    print(count_people(students))



def count_people(students):
    for i in range(len(students)):
        print(i+1, students[i])
main()


