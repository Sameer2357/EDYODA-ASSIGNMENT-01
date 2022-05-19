# 1 Python program to capitalize the first and last character of each word in a string (input string should be a statement)

ch=input("Enter the String:")
j=0
str=list(ch)
str+='\0'
for i in range(len(str)):
    if i==0 or str[i-1]==' ':
        str[i]=str[i].upper()
    elif str[i]==' ' or str[i]=='\0':
        str[i-1] = str[i-1].upper()

print("Your String is:", "".join(str))







# 2 Python program to count the number of vowels in a given string.

# string=input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)






   
# 3 Program to check if a string contains any special character.

# import re
# string = input('Enter any string: ')
# special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
# if(special_char.search(string) == None):
#     print('String is accepted.')
# else:
#     print(' string is not accepted.')