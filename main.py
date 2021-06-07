from math import pi
from datetime import date

def calculate_radius():
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

def reverse_name():
    fname = input("Input your First Name : ")
    lname = input("Input your Last Name : ")
    print("Your reverse name is   " + lname + " " + fname)

def current_date_time():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Current ate and time =", d2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_radius()
    print("---------------------------")
    reverse_name()
    print("---------------------------")
    current_date_time()