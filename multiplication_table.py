number = int(input("Enter a number: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

if start <= 0 or end <= 0:
    print("Error: Start and end must be positive numbers.")
elif start >= end:
    print("Error: Starting range must be smaller than ending range.")
else:
    print("\n--- Multiplication Table ---")

    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")
