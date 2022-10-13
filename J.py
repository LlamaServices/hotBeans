starting_number = int(input())
number = starting_number
while True:
    number = sum([int(x)**2 for x in str(number)])
    if number == starting_number:
        print("ne")
        break
    if number == 1:
        print("da")
        break

