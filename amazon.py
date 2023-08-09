# This program writes a new line in the new text file output.txt for each line in input.txt,
# that computes the answer to some operation on a list of numbers.

# Defining functions min, max, and avg

def minimum(list):

    return min(list)

def maximum(list):

    return max(list)

def average(list):

    result = sum(list) / len(list)

    return round(result, 2) # I tried to round the result but it keeps giving me 3.5 instead of 3.4 as the PDF for this task shows

# Reading the content of the text file input.txt

input_file = open('input.txt', 'r', encoding='utf-8-sig')

f = input_file.readlines()

input_file.close()

# Working on each line of input file

for line in f:

    full_line = line.split(':')

    command = full_line[0]
    numbers = full_line[1]

    numbers_split = numbers.strip('\n').split(',')

    final_numbers = []

    for num in numbers_split:

        final_numbers.append(int(num))

# Writing the content on the text file output.txt

    if command == 'min':

        output_file = open('output.txt', 'a', encoding='utf-8-sig')

        output_file.write((f"The min of {final_numbers} is {minimum(final_numbers)}\n"))

        output_file.close()

    elif command == 'max':

        output_file = open('output.txt', 'a', encoding='utf-8-sig')

        output_file.write((f"The max of {final_numbers} is {maximum(final_numbers)}\n"))

        output_file.close()

    elif command == 'avg':

        output_file = open('output.txt', 'a', encoding='utf-8-sig')

        output_file.write((f"The avg of {final_numbers} is {average(final_numbers)}\n"))

        output_file.close()
