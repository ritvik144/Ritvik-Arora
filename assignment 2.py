print('Q1')
#giving value to input string#
input_str= 'Python is a case sensitive language'

#finding length of the string#
print('\npart a')
print('Length of the string is : ', len(input_str))

#printing input_str in reverse order#
print('\npart b')
print(' The string in reverse order is :', input_str[ : : -1])

#slicing and printing the sliced string#
print('\npart c')
sliced_str= input_str[10:26]
print('The sliced string is:', sliced_str)

#replacing and printing the new string#
print('\npart d')
new_str= input_str.replace(" a case sensitive ", " object oriented ")
print('The new string is : ', new_str)

#printing index of 'a'#
print('\npart e ')
print(input_str.index("a"))

#removing the white spaces from the input string#
print('\npart f')
print(input_str.replace(" ", ""))

###############################################################################

print('\nQ2')
#initialising variables#
name= "Ritvik Arora"
SID= "21105033"
Branch= "ECE"
CGPA= "9"
#printing the output#
print(f"Hey, {name.title()} here! \nMy SID is {SID} \nI am from {Branch} department and my CGPA is {CGPA} ")

###############################################################################

print('\nQ3')

#assigning values#
a=65
b=10

print('\npart a ')
print(' a&b : ', a&b)

print('\npart b')
print(' a|b : ', a|b)

print('\npart c')
print(' a^b : ', a^b)

print('\npart d')
print('Left shift a by 2 bits :', a<<2)
print('\n Left shift b by 2 bits :', b<<2)

print('\npart e')
print('Right shift a by 2 bits :', a>>2)
print('Right shift b by 4 bits :', b<<4)

#############################################################################

print ('\nQ4')
#taking inputs from the user#

a= int(input('enter first no. '))
b= int(input('enter second no. '))
c= int(input('enter third no. '))
#finding the largest no. #

if(a>b):
        if(a>c):
            print('The largest no. is ', a)
        else:
            print(' The largest no. is ', c)

else:
       if(c>b):
           print(' The largest no. is ', c)
       else:
           print(' The largest no. is ', b)
 #############################################################################
print('\nQ5')
#taking input string from user#

input_str= input("Enter the string ")
if "name" in input_str :
    print('yes')
else:
    print('no')
############################################################################
print('\nQ6')
#taking input from user#
a= int(input('\nEnter length of first side: '))
b= int(input('\nEnter length of second side: '))
c= int(input('\nEnter length of third side: '))
#applying the conditions for the output#

if a+b>c and b+c>a and a+c>b :
    print('Yes, triangle can be formed with these values')
else:
    print('No, triangle cannot be formed with these values')
###########################################################################


           
            
            
      




