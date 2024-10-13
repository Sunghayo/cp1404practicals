def main():

    numbers = [3, 1, 4, 1, 5, 9, 2]

    print(numbers[0])  # 3
    print(numbers[-1])  # 2
    print(numbers[3])  # 1
    print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
    print(numbers[3:4])  # [1]
    print(5 in numbers)  # True
    print(7 in numbers)  # False
    print("3" in numbers)  # False (since it's a string, not an integer)
    print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    numbers[0] = "ten"  # Change the first element to "ten" (string)
    numbers[-1] = 1  # Change the last element to 1
    print(numbers[2:])  # Print all elements except the first two (slice)
    print(9 in numbers)  # Print whether 9 is an element of the list


main()