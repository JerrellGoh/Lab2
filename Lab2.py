# Lab2.py

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter numbers: ")
    num_list = user_input.split(",") 
    num_list = [float(x)for x in num_list]  # Convert to float
    
    return num_list
def calc_average_temperature(num_list):
    average = sum(num_list) / len(num_list)
    print("Average temperature:", average)
    return average

def calc_min_max_temperature(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    print("Minimum temperature:", min_temp)
    print("Maximum temperature:", max_temp)
    return min_temp, max_temp

def main():
    print("# Calculator")
    display_main_menu()
    num_list = get_user_input()
    if num_list:
        calc_average_temperature(num_list)
        calc_min_max_temperature(num_list)

if __name__ == "__main__":
    main()
