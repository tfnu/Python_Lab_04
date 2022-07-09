# This application validates the

# Programmer Information
# Name: FNU Tripti
# A-ID: A20503656
# Course: ITMD-513
# Date: 07/04/2022
# Lab #: 4


# if the card number is valid, this function returns true
import sys
from datetime import date

def isValid(number):
    if number.isalpha():
        return -1
    elif any(c.isalpha() for c in number):
        return -2
    elif number.isnumeric():
        # Check for the length of the credit card numbers using the getSize method
        if getSize(number) < 13:
            return -3
        elif getSize(number) > 16:
            return -4
        else:
            return 4


# obtain the result from Step 2
def sumOfDoubleEvenPlace(number):
    # Reversing the string to calculate the right to left calculations (Reference: Textbook)
    reverse_number = number[::-1]

    # Iterating over the digits in a number
    place = 1
    double_some_even_digits = 0
    for i in reverse_number:
        if place % 2 == 0:
            # Accumulating the doubled sum also calling the function if the digit becomes 2-digit number
            double_some_even_digits = double_some_even_digits + getDigit(2 * int(i))
        place = place + 1
    return double_some_even_digits


# if variable number is a single digit, then return the number
# otherwise, return number as the sum of the two digits
def getDigit(number):
    if number < 10:
        return number
    else:
        sum_of_digits = (number % 10) + (number // 10)
        return sum_of_digits


# this function returns the sum of odd place digits in variable number
def sumOfOddPlace(number):
    # Reversing the string to calculate the right to left calculations (Reference: Textbook)
    reverse_number = number[::-1]

    # Iterating over the digits in a number
    place = 1
    some_odd_digits = 0
    for i in reverse_number:
        if place % 2 != 0:
            some_odd_digits = some_odd_digits + int(i)
        place = place + 1
    return some_odd_digits


# if the digit d is a prefix for variable number, then return true
def prefixMatched(number):
    prefix = ""
    for x in number:
        if int(x) == 3:
            prefix = getPrefix(number, 2)
            break
        else:
            prefix = getPrefix(number, 1)
            break
    return prefix


# this function returns the number of digits in variable d
def getSize(d):
    return len(d)


# returns the first k number of digits from variable number but if the
# number of digits in variable number is less than k, return number
def getPrefix(number, k):
    prefix = ""
    if int(number) < k:
        return k
    else:
        count = 1
        for x in number:
            prefix += x
            if count >= k:
                break
            count = count + 1
        return prefix


def getFinalValidation(number):
    if number % 10 == 0:
        return True
    else:
        return False


# This method is used to the input the credit card number.
def inputCreditCardNumber():
    print("Please input the credit card number:")
    cc_number = input()
    return cc_number.replace(" ", "")


if __name__ == "__main__":

    print("This program for course ITMD-513 is executed by FNU Tripti (A20503656) on : ", date.today())

    cc_number = inputCreditCardNumber()

    # Calling the isValid function to validate the inout number
    is_valid = isValid(cc_number)

    if is_valid == -1:
        print("The Credit Card Number contains only alphabets; This is not a valid Credit Card.")
    elif is_valid == -2:
        print("The Credit Card Number contains alphabets; This is not a valid Credit Card.")
    elif is_valid == -3:
        print("The length of the card is less than 13 digits. This is not a valid Credit Card.")
    elif is_valid == -4:
        print("The length of the card is more than 16 digits. This is not a valid Credit Card.")
    elif is_valid == 4:
        print("The Credit Card entered has a valid length and does not contain any alphabets.")

        # Calculation of the Company which issued the card.
        prefix = prefixMatched(cc_number)

        if prefix == "37":
            print("The Card is an AMERICAN EXPRESS Card.")
        elif prefix == "6":
            print("The Card entered is a DISCOVER Card.")
        elif prefix == "5":
            print("The Card entered is a MASTER Card.")
        elif prefix == "4":
            print("The Card entered is a VISA Card.")
        else:
            print("The Card is Invalid; And Is not issued by a valid Company in the list")
            sys.exit()

        sum_of_doubled_even_places = sumOfDoubleEvenPlace(cc_number)
        print("The sum of even digits doubled is : ", sum_of_doubled_even_places)
        sum_of_odd_place_digits = sumOfOddPlace(cc_number)
        print("The sum of odd digits is : ", sum_of_odd_place_digits)
        total_sum = sum_of_doubled_even_places + sum_of_odd_place_digits
        final_validation = getFinalValidation(total_sum)
        if final_validation:
            print("The Card is Valid; As it satisfies all the conditions and Luhn's Formula as well.")
        else:
            print("The Card is Invalid; Because it Fails to satisfy the Luhn's formula.")
