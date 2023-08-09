# Input-Output Text File Processor

This program processes commands from an `input.txt` file to compute minimum, maximum, and average of lists of numbers and outputs the result to an `output.txt` file.

## How it Works

1. The program reads from an `input.txt` file where each line is of the form: `<command>:<list_of_numbers>`.
    - For example: `min:1,2,3,4,5`
2. For each line in the `input.txt` file, it computes the specified operation on the list of numbers.
3. The results are then written to an `output.txt` file in the format: `The <command> of [<list_of_numbers>] is <result>`.
    - For the above example: `The min of [1, 2, 3, 4, 5] is 1`

## Available Commands

- **min**: Computes the minimum of the list of numbers.
- **max**: Computes the maximum of the list of numbers.
- **avg**: Computes the average of the list of numbers and rounds to two decimal places.

## Setup & Execution

1. Ensure you have a Python environment set up.
2. Create an `input.txt` file in the same directory as the program. Add your commands and numbers in the format mentioned above.
3. Run the program.
4. Check the `output.txt` file for the results.

## Note

- There seems to be a discrepancy with the rounding function in the `average` function as pointed out in the program's comments. The program might not always give the expected rounding as shown in certain documentation. Ensure to verify the results manually if needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
