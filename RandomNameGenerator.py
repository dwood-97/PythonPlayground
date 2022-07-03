import string
import random

cust_name = input("Hello! Thank you for using our EC2 instance name generator.\nWhat is your name?\n\n")
depts = ["accounting", "marketing", "finops"]
print("\nNice to meet you, " + cust_name.capitalize() + "!")
dept_name = input("What department do you work for?\n\n").lower()

if dept_name not in depts:
    print("I'm sorry but it looks like your department does not have access to this program.")
    
if dept_name in depts:
    print("\nGreat! Thank you for being a part of the " + dept_name.capitalize() + " team!")
    
ec2_name = input("How many instance names can I make for you today " + "?\n\n")
print("\nPerfect, here are your instance names: ")

ec2_name = int(ec2_name)
for _ in range(ec2_name):

    n = random.randint(0, 100000000)
    print(dept_name[ 0 : 4].upper(),"_",str(n))