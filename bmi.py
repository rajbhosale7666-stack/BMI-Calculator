# BMI Calculator Project

print("===== BMI Calculator =====")

try:
    # Taking user input
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Input validation
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        # BMI Calculation
        bmi = weight / (height ** 2)

        print(f"\nYour BMI is: {bmi:.2f}")

        # Categorization
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        print("Category:", category)

except ValueError:
    print("Invalid input! Please enter numeric values only.")

