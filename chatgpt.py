def main():
    try:
        n = int(input("How many numbers do you want to add? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n <= 0:
        print("The number of entries should be positive.")
        return

    n_sum = []
    total_sum = 0

    for i in range(1, n + 1):
        while True:
            try:
                number = float(input(f"Please enter number {i}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        n_sum.append(number)
        total_sum += number

    print("Numbers entered:", n_sum)
    print("Type of the list:", type(n_sum))
    print("Total sum:", total_sum)

if __name__ == "__main__":
    main()
