from utils import square, is_even, celsius_to_fahrenheit


def main():
    try:
        user_input = float(input("Enter a number: "))

        sq_val = square(user_input)
        even_status = "even" if is_even(user_input) else "odd"
        fah_val = celsius_to_fahrenheit(user_input)

        print(f"\n--- Results for {user_input} ---")
        print(f"Square: {sq_val}")
        print(f"Even/Odd: The number is {even_status}.")
        print(f"As Celsius in Fahrenheit: {fah_val:.2f}°F")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
