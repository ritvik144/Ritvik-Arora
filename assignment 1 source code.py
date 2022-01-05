#Q1#
print('Q1')
num1= int(input('enter first no. '))
num2= int(input('enter second no. '))
num3= int(input('enter third no. '))                               #taking the numbers from the user#

avg= (num1+num2+num3)/3                                            #defining the formula for average#
 
print(' The average of numbers is ' , avg )                        # displaying  the result#

#Q2#
print('Q2')

gross = int(input(' Enter your gross income to the nearest penny '))
dep= int(input(' Enter the total number of dependants '))        # taking the required inputs from the user#

taxable = (gross)- 10000 - (dep*3000)

tax=(taxable)*(0.2)                                                #formula#

if tax<0 :
    print('The total income tax is 0$\n')
else :
    print('The total income tax is ',tax)

#Q3#
print('Q3')

SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))                              #inputs from the user#

Student=[SID,name,gender,course,cgpa]                             #list#

print(Student)

#Q4#
print('Q4')
m1=float(input("enter the marks of 1st student="))
m2=float(input("enter the marks of 2nd student="))
m3=float(input("enter the marks of 3rd student="))
m4=float(input("enter the marks of 4th student="))       
m5=float(input("enter the marks of 5th student="))                #inputs from the user#
marks=[m1,m2,m3,m4,m5]
marks.sort()
print(marks)                                                      #sorted marks#

#Q5(a)#
print('Q5(a)')
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Black')
print(color)

#Q5(b)#
print('Q5(b)')
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=['Purple']
print(color)


        





