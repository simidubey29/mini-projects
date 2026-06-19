
# BMI Calculator
# Author: Simi Dubey

def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("=" * 40)
print("        BMI CALCULATOR")
print("=" * 40)

try:
    name = input("Enter your name: ")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    if weight <= 0 or height <= 0:
        print("\nWeight and height must be greater than zero.")
    else:
        bmi = calculate_bmi(weight, height)

        print("\n----- RESULT -----")
        print(f"Name      : {name}")
        print(f"Weight    : {weight} kg")
        print(f"Height    : {height} m")
        print(f"BMI       : {bmi:.2f}")
        print(f"Category  : {bmi_category(bmi)}")

except ValueError:
    print("\nPlease enter valid numeric values.")
