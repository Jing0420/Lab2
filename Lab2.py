def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    print("Average of the list =", round(average, 2))
    min_max = find_min_max(num_list)
def display_main_menu():
    print("Enter some numbers separated by commas(e.g.5,67,32)")
def get_user_input():
    x = input("Enter some numbers")
    print(x)
    txt = (""+x)
    y = txt.split()
    print(y)
    num_list = list(map(float, y))
    print(num_list)
    return num_list
def calc_average(num_list):
    print("calc_average")
    average = sum(num_list)/len(num_list)
    return average
def find_min_max(float_list):
    print("find_min_max")
    print("Maximum of the list is :", end="")
    print(max(float_list))
    print("Minimum of the list is :", end="")
    print(min(float_list))
    return max(float_list) and min(float_list)
if __name__ == "__main__":
    main()