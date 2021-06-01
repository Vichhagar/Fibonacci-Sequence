def fibonacci(n):
    num_1 = 1
    num_2 = 0

    sequence = [0]

    while len(sequence) <= n:
        num_1 += num_2
        sequence.append(num_1)

        num_2 += num_1
        sequence.append(num_2)

    print("Length: " + str(len(sequence) - 1))
    return sequence


count = int(input("How many number you want in your sequence: "))
number = fibonacci(count)

counter = 0
for i in number:
    print(counter, i)
    counter += 1



