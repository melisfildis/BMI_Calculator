def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    if bmi <= 18.4:
        print("You are underweight.")
    elif bmi <= 24.9:
        print("You are healthy.")
    elif bmi <= 29.9:
        print("You are overweight.")
    elif bmi <= 34.9:
        print("You are severely overweight.")
    elif bmi <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")

    return bmi

weight = float(input("Enter your weight: ")) #Weight should be in kilograms.
height = float(input("Enter your height: ")) #The height should be written in meters for example: 1.60
result = calculate_bmi(weight, height)
print("Your BMI is:", result)
