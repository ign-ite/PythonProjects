height = float(input("Enter your height in meter: "))
weight = int(input())
bmi = (weight / (height*height))
if (bmi < 18.5):
    print("Underweight")
elif (18.5 <= bmi < 25):
    print("Normal weight")
elif (25 <= bmi < 30):
    print("Slightly Overweight")
elif (30 <= bmi < 35):
    print("Obese")
elif (bmi >= 35):
    print("Clinically Obese")