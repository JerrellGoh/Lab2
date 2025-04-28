def calculate_bmi(height, weight): 
    print("Height = " + str(height) )
    print("Weight = " + str(weight) )
    bmi = weight / (height ** 2)
    return bmi 

def classify_bmi(bmi_value):
    if bmi_value >25.0 :
        print("Overweight")
        return 1 
    elif bmi_value > 18.5 and bmi_value < 25.0:
        print("Normal weight")
        return 0
    else:
        print("underweight")
        return -1
    
def main():
    height = input("Enter height in meters: ")
    height = float(height)
    weight = input("Enter weight in kg: ")
    weight = float(weight)
    bmi_output = calculate_bmi(height, weight)
    classify_bmi(bmi_output)
    print("bmi_value:" +str(bmi_output))

if __name__ == "__main__":
    main()