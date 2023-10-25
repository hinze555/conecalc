def tower_calculation(n, max_mult):
    # Calculate multiplication
    tower_up = [int(n)]
    for i in range(2, max_mult + 1):
        n *= i
        tower_up.append(int(n))

    # Calculate division
    tower_down = [tower_up[-1]]
    for i in range(2, max_mult + 1):
        n /= i
        tower_down.append(int(n))

    tower_down = tower_down[:-1]  # Removing the last division which results in the initial number
    return tower_up, tower_down

def has_repeated_digits(n):
    """Check if the number has any repeated digit."""
    return len(set(n)) != len(n)

def main():
    while True:
        # Ask the user for number input
        num = input("Please enter a number: ")

        # Check if input contains 1, 5, 0 or repeated digits
        if any(x in num for x in ['1', '5', '0']) or has_repeated_digits(num):
            print("Please enter a number without the digits 1, 5, 0 and without repeated digits.")
            continue
        num = int(num)
        break

    # Ask the user for the maximum multiplication level
    max_mult = int(input("Please enter the maximum multiplication level (e.g. 9 for *2 up to *9): "))

    tower_up, tower_down = tower_calculation(num, max_mult)
    max_width = len(str(tower_up[-1]))  # Maximum width for formatting purposes

    # Displaying multiplication results
    for i, value in enumerate(tower_up[:-1]):
        print(f"{value:>{max_width}} * {i+2}")

    # Displaying division results
    for i, value in enumerate(tower_down):
        print(f"{value:>{max_width}} / {i+2}")

    print(f"{num:>{max_width}}")

if __name__ == "__main__":
    main()
