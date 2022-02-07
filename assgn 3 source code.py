print('Q1\n')
input_value = input("Enter the string: ").lower().split()
if len(input_value) == 1:
    input_value = input_value[0]
occurences = {}
for i in input_value:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print("The occurence(s) of:")
for i in occurences:
    print('\t%s is/are %d' % (i,occurences[i]))

    
print('Q2\n')
date= int(input('Enter the date '))
month= int(input('Enter the month '))
year = int(input('Enter the year '))

if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                 
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")


if (year%400==0):
    leap_year= True
elif (year%100==0) :
    leap_year= False
elif (year%4==0):
    leap_year= True

if month in (1,3,5,7,8,10,12):
    month_length= 31
elif month==2:
    if  (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        month_length= 29
    else :
        month_length= 28

else:
    month_length=30
if (month<1 or month>12) :
    print('Enter valid input')
elif (year<1800 or year>2025):
    print('Enter valid input')

elif (date< month_length):
    date= date+1
    print("The next date is %d/%d/%d" % (date, month, year))

elif (date== month_length) :
    date = 1
    if month==12:
        month=1
        year=year+1
        print("The next date is %d/%d/%d" % (date, month, year))
    else:
        month=month+1
        print("The next date is %d/%d/%d" % (date, month, year))


else:
    print('Enter valid input')


print('Q3\n')

list_in = eval(input("Enter the list: "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))
print("Output:", list_out)

print('Q4\n')
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                              
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and '%s' Performance" % (i[0],i[1]))

print('Q5\n')

string = "ABCDEFGHIJK"
j = 0
while len(string)-j*2 >= 1:
    print(" "*j, string[0 : len(string) - j*2])
    j += 1

print('Q6\n')
dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    more_data = input("Do you want to enter more data? ")
    if more_data in ("N","n","No","no","NO"):
        break
print("\na. Student Details:")                                                                                      
for i in dict1:
    print("The SID of %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                                                                                              
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue

print('Q7\n')
n=int(input('Enter the no. of terms: '))
a=0
b=1
total=0
if n<= 0 :
    print('kindly enter valid input')
elif n==1 :
    print(' the term is 0 and hence avg is also 0')
else :
    print(a)
    

    for  i in range(1,n):

        
        total=total+b
    
        print(b)
        c=a+b
        a=b
        b=c
print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (n,total/n))

print('Q8\n')
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
        
        

      
        
        
    
   

        
    




 



    

    
