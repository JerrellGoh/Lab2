def calculate_bmi(height, weight): 
    print("Height = " + str(height) )
    print("Weight = " + str(weight) )
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi) )

    if bmi >25.0 :
        print("Overweight")
        return 1 
    elif bmi > 18.5 and bmi < 25.0:
        print("Normal weight")
        return 0
    else:
        print("underweight")
        return -1

calculate_bmi(weight=57, height=1.73)
