# Task 1
name = input("Enter your name: ")
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# Task 2
in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Task 3
with open('numbers.txt', 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())

result = first_number + second_number
print(result)

# Task 4
total = 0
with open('numbers.txt', 'r') as in_file:
    for line in in_file:
        total += int(line)

print(total)