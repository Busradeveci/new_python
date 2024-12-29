import math


def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    while True:
        print("\nEnter the coordinates of two points:")
        try:
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))

            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            print(f"The Euclidean distance between the points is: {distance:.2f}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        choice = input("Do you want to calculate another distance? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
