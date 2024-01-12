def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    first_digit = int(input("Enter your first number: "))
    second_digit = int(input("Enter your second number: "))

    result = sum_of_two_digits(first_digit, second_digit)

    print("Sum: ", result)
