# This code is written to calculate Body Mass Index of a person. Feel free to check your BMI
name = input("Enter your name")

weight = int(input('Enter your weight in pounds: '))

height = int(input('Enter your height in inches: '))

# to find bmi is (weight in pounds * 703) / (height in inches * height in inches)
BMI = (weight * 703) / (height * height)

if BMI > 0:
    # BMI	Weight Status
    # Below 18.5	Underweight
    # 18.5 – 24.9	Healthy Weight
    # 25.0 – 29.9	Overweight
    # 30.0 and Above	Obesity
    if BMI < 18.5:
        print(name + " ,Your BMI is", BMI, ",You are underweight!")
    elif BMI <= 24.9:
        print(name + " ,Your BMI is", BMI, ",You are normal weight")
    elif BMI <= 29.9:
        print(name + " ,Your BMI is", BMI, ",You are overweight")
    elif BMI <= 34.9:
        print(name + " ,Your BMI is", BMI, ",You are obese")
    elif BMI <= 39.9:
        print(name + ", Your BMI is", BMI, ",You are severely obese")
    else:
        print(name + ", Your BMI is", BMI, ",You are morbidly obese ")
else:
    print('Enter valid input')
