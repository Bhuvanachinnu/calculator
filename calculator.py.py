print('Select an Operator to perform')
print('1.Add')
print('2.Subtract')
print('3.Multiplication')
print('4.Division')
operation=input()
if operation=='1':
    num1=input('Enter first number')
    num2=input('Enter Second number')
    print("The sum is "+str(int(num1)+int(num2)))
elif operation=='2':
    num1=input('enter first number')
    num2=input('enter Second number')
    print("The subtract is" +str(int(num1)-int(num2)))
elif operation=='3':
    num1=input('enter first number')
    num2=input('enter Second number')
    print("the division "is +str(int(num1)/int(num2)))
elif operation=='4':
    num1=input('enter first number')
    num2=input('enter Second number')
    print("the division is "+str(int(num1)%int(num2)))
else:
    print('Invalid Syntax')
