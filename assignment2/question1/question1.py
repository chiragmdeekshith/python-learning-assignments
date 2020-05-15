def find_max_min(*args):

    count = 0
    total_sum = 0
    minimum = args[0]
    maximum = args[0]

    for number in args:
        count += 1
        total_sum += number
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    print("Count = ", count)
    print("Total sum = ", total_sum)
    print("Minimum = ", minimum)
    print("Maximum = ", maximum)
