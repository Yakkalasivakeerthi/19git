#Implement a menu-driven program where the user can  choose to:
while True:
    print('1.Addition 2.Subtraction 3.Multiplication 4.Division. Another option will exit the code')
    choice = input('Enter your choice: ')
    if choice == '1' or choice == 'Addition':
        input_num1 = float(input('Enter the number to Addition: '))
        input_num2 = float(input('Enter the number to Addition: '))
        print(input_num1+input_num2)
    elif choice == '2' or choice == 'Subtraction':
        input_num1 = float(input('Enter the number to Subtraction: '))
        input_num2 = float(input('Enter the number to Subtraction: '))
        print(input_num1-input_num2)
    elif choice == '3' or choice == 'Multiplication':
        input_num1 = float(input('Enter the number to Multiplication: '))
        input_num2 = float(input('Enter the number to Multiplication: '))
        print(input_num1*input_num2)
    elif choice == '4' or choice == 'Division':
        input_num1 = float(input('Enter the number to Division: '))
        input_num2 = float(input('Enter the number to Division: '))
        print(input_num1/input_num2)
    else:
        print('No valid option picked')
        print('----Exiting---')
        break

# Factorial program:
num = int(input())
factorial = 1
n = num
while n > 1:
    factorial *= n
    n -= 1
print(f"Factorial of {num} is {factorial}")


#Reverse a number using a while loop.
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
num=int(input())
result=reverse(num)
print(result)

#prinr all numbers that are divisible by a and 5 from 1 to 100
num=1
while num<=100:
    if num%3==0 and num%5==0:
        print(num,end=' ')
    num+=1

# Login page:
def login():
    username=input("Enter your username: ")
    savedPassword="123456"
    count=1
    while count<4:
        count+=1
        password=input("Enter your password here: ")
        if password==savedPassword:
            print("Login Successfull")
            break
        elif password!=savedPassword:
            print(f"Wrong Password, You have {4-count} more attempts left")
            if count==4:
                print("You have exhaused your login attempts. Revisit after 24hrs.")
        else:
            print("Something went wrong")
            break
login()

        
    
