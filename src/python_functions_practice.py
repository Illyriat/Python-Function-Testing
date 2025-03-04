from datetime import datetime


def return_10():
    return 10

def add(num_1, num_2):
    result =  num_1 + num_2
    return result

def subtract(num_1, num_2):
    result = num_1 - num_2
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result

def divide(num_1, num_2):
    result = num_1 / num_2
    return result

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(str_num_1, str_num_2):
    num_1 = int(str_num_1)
    num_2 = int(str_num_2)
    add_result = num_1 + num_2
    return add_result

def number_to_full_month_name(month_num):
    date_time_object = datetime.strptime(str(month_num), "%m")
    date_time_string = date_time_object.strftime( "%B")
    return date_time_string

# Class solution
# def test_number_to_full_name_month_1(self):
#     result = number_to_full_month_name ( 1 )
#     self.assertEqual( "January", result )

# def test_number_to_full_name_month_3(self):
#     result = number_to_full_month_name ( 3 )
#     self.assertEqual( "March", result )

def number_to_short_month_name(month_num):
    date_time_object = datetime.strptime(str(month_num), "%m")
    date_time_string = date_time_object.strftime( "%b")
    return date_time_string

# Class Solution
# def test_number_to_short_month_name_month(self):
#     first_month_string = number_to_short_month_name ( 1 )
#     self.assertEqual ("Jan", first_month_string)

#  Further

def volume_of_cube(length_of_side):
    return length_of_side **3


def reverse_string(str):
    return str[::-1]


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9