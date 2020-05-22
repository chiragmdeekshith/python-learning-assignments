from assignment1 import assignment1
from assignment2 import assignment2
from assignment3 import assignment3


def main():
    while True:
        print("""\n\nEnter the assignment number that you want to run:-
            1) Assignment 1
            2) Assignment 2
            3) Assignment 3
            0) Exit""")
        option = input()
        option = int(option)

        if option == 1:
            print("Assignment 1:-")
            assignment1.main()

        elif option == 2:
            print("Assignment 2:-")
            assignment2.main()

        elif option == 3:
            print("Assignment 3:-")
            assignment3.main()

        elif option == 0:
            print("Exiting.")
            break

        else:
            print("Wrong option, please try again")

    del option


main()
