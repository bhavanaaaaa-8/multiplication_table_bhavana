# Multiplication Table Generator
## Description
This Python program accepts a number from the user and generates its multiplication table within a range specified by the user.

The program also validates the range to make sure that:
- The starting number is positive.
- The ending number is positive.
- The starting number is smaller than the ending number.

## Features
- Accepts a number from the user.
- Allows the user to choose the starting and ending range.
- Uses a `for` loop to generate the table.
- Validates the user's range.
- Displays the multiplication table clearly.

## How to Run
1. Make sure Python is installed on your computer.
2. Run the Python file.
3. Enter the number for which you want the multiplication table.
4. Enter the starting range.
5. Enter the ending range.
6. The program will display the multiplication table.

## Example

### Input
```text
Enter a number: 7
Enter the starting range: 3
Enter the ending range: 8
```

### Output
```text
--- Multiplication Table ---
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
```

## Validation Examples
```text
Starting range: -2
Ending range: 10
Error: Start and end must be positive numbers.
```

```text
Starting range: 10
Ending range: 5
Error: Starting range must be smaller than ending range.
```
- `input()`
- `int()`
- `if-
