# create simple system to calculate loan amount to be disbursed
# define variables:
first_name = input("Enter your first_name: ")
last_name = input("Enter your last_name: ")
email_address = input("Enter your active email_address: ")
id_no = input("Enter your di number: ")
salary = int(input("Enter your current salary: "))

# Loans can be given for employees whose salary is greater than 25000
if salary >= 25000:
    print("You qualify for a loan of upto Kshs 100,000 and above")
else:
    print("Dear",first_name,"You do not qualify for a loan. Please try again later! ")
