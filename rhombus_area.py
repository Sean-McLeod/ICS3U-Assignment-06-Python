#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program calculates the area of a rhombus


def rhombus_area(first_diagonal, second_diagonal):
    # this function calculates the area of a rhombus

    # process
    area = (first_diagonal*second_diagonal)/2

    return area


def main():
    # this function gets the two diagonals

    print("This program calculates the area of a rhombus")
    print("\n")

    # input
    user_first_diagonal = input("Enter in the first diagonal(cm): ")
    user_second_diagonal = input("Enter in the second diagonal(cm): ")
    print("\n")

    try:
        int_first_diagonal = int(user_first_diagonal)
        int_second_diagonal = int(user_second_diagonal)

        if int_first_diagonal > 0 and int_second_diagonal > 0:
            # call functions
            final_rhombus_area = rhombus_area(int_first_diagonal,
                                              int_second_diagonal)

            # output
            print("The area of this rhombus is {}cm²"
                  .format(final_rhombus_area))

        else:
            print("The values should be positive")

    except Exception:
        print("This is an invalid number. Please try again")


if __name__ == "__main__":
    main()
