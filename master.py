from assignment1 import assignment1
from assignment2 import assignment2
from assignment3 import assignment3


def main():
    while True:
        print("""\n\nEnter the assignment number that you want to run:-
            1) Assignment 1
            2) Assignment 2
            3) Assignment 3
            4) Assignment 4
            5) Assignment 5
            6) Assignment 6
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

        elif option == 4:
            print("Assignment 4:-")
            print("Run the assignment4.py for server and the client.py file for client. Run the send_chat_log.py to "
                  "send chat logs to email IDs")

        elif option == 5:
            print("Assignment 5:-")
            print("Run the assignment5.py for flask server. Open index.html for UI.")

        elif option == 6:
            print("Assignment 6:-")

        elif option == 0:
            print("Exiting.")
            break

        else:
            print("Wrong option, please try again")

    del option


main()
