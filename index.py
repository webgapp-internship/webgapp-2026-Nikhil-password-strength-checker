# # vowels="aeiou"
# # username=input("enter your name : ")
#  # # # # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # # # # # for i in username:
# # # # # # # # # # # # # # # # # # #  if i in vowels:
# # # # # # # # # # # # # # # # # # #   count=count+1
# # # # # # # # # # # # # # # # # # # print(count)


#  # # # # # # # # # # # # # # # email=input("enter your email ID : ")
# # # # # # # # # # # # # # # # # # if '@' in email:
# # # # # # # # # # # # # # # # # #     print("Your email is valid")
# # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # #     # print("your email is invalid ")

# # # # # # # # # # # # # # # # # strings="AC30BD40"
# # # # # # # # # # # # # # # # letters=""
# # # # # # # # # # # # # # # # # digits=""
# # # # # # # # # # # # # # # # # for i in strings:
# # # # # # # # # # # # # # # # #     if i.isalpha():
# # # # # # # # # # # # # # # # #         letters=letters+i
# # # # # # # # # # # # # # # # #     elif i.isdigit():
# # # # # # # # # # # # # # # # #         digits=digits+i
# # # # # # # # # # # # # # # # # print(letters)
# # # # # # # # # # # # # # # # # print(digits) 
# # # # # # # # # # # # # # # # # for i in digits:
# # # # # # # # # # # # # # # # #     sumdigits=0
# # # # # # # # # # # # # # # # # for k in digits:
# # # # # # # # # # # # # # # # #     sumdigits=int(k)+sumdigits
# # # # # # # # # # # # # # # # # newchar=letters+str(sumdigits)
# # # # # # # # # # # # # # # # # print(newchar)


# # # # # # # # # # # # # # # # num=int(input("enter a number"))
# # # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # # for i in range(num,0,-1):
# # # # # # # # # # # # # # # #     count=count+i
# # # # # # # # # # # # # # # # print(count)


# # # # # # # # # # # # # # # def add(a,b):
# # # # # # # # # # # # # # #     c=a+b
# # # # # # # # # # # # # # #     print(c)
# # # # # # # # # # # # # # # add(10,30)


# # # # # # # # # # # # # # def check_password_strength(pwd):
# # # # # # # # # # # # # #     import re
# # # # # # # # # # # # # #     if (len(pwd) >= 8 and
# # # # # # # # # # # # # #         re.search(r"[A-Z]", pwd) and
# # # # # # # # # # # # # #         re.search(r"[a-z]", pwd) and
# # # # # # # # # # # # # #         re.search(r"[0-9]", pwd) and
# # # # # # # # # # # # # #         re.search(r"[!@#$%^&*()_+]", pwd)):
# # # # # # # # # # # # # #         return "Strong"
# # # # # # # # # # # # # #     return "Weak"
# # # # # # # # # # # # # # a=input("enter the password : ")
# # # # # # # # # # # # # # print(check_password_strength(a))


# # # # # # # # # # # # # for i in range(1,6):
# # # # # # # # # # # # #     for j in range(1,i+1):
# # # # # # # # # # # # #         print(j,end=" ")
# # # # # # # # # # # # #     print()  


# # # # # # # # # # # correct_user = "admin"
# # # # # # # # # # # correct_pass = "1234"

# # # # # # # # # # # while True:
# # # # # # # # # # #     user = input("Enter username: ")
# # # # # # # # # # #     pwd =input("Enter password: ")

# # # # # # # # # # #     if user == correct_user and pwd == correct_pass:
# # # # # # # # # # #         print("Login Successful")
# # # # # # # # # # #         break
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("Wrong credentials, try again!")


# # # # # # # # # # rows = 5
# # # # # # # # # # for i in range(1, rows + 1):
# # # # # # # # # #     for j in range(rows - i):
# # # # # # # # # #         print(" ", end="")
# # # # # # # # # #     for k in range(i):
# # # # # # # # # #         print("* ", end="")
# # # # # # # # # #     print()


# # # # # # # # # nums = [10, 20, 30, 40]

# # # # # # # # # for i in nums:
# # # # # # # # #     print(i)


# # # # # # # # nums = [1, 2, 3, 4]
# # # # # # # # rev = []

# # # # # # # # for i in nums:
# # # # # # # #     rev = [i] + rev

# # # # # # # # print("Reversed:", rev)


# # # # # # # nums = [1, 2, 2, 3, 4, 4]
# # # # # # # unique = []

# # # # # # # for i in nums:
# # # # # # #     if i not in unique:
# # # # # # #         unique.append(i)

# # # # # # # print(unique)



# # # # # # students = {}

# # # # # # while True:
# # # # # #     print("\n1. Add Student")
# # # # # #     print("2. View Students")
# # # # # #     print("3. Search Student")
# # # # # #     print("4. Delete Student")
# # # # # #     print("5. Exit")

# # # # # #     choice = input("Enter choice: ")

# # # # # #     if choice == "1":
# # # # # #         roll = input("Enter Roll No: ")
# # # # # #         name = input("Enter Name: ")
# # # # # #         mark = input("Enter Marks: ")

# # # # # #         students[roll] = {
# # # # # #             "name": name,
# # # # # #             "mark": mark
# # # # # #         }

# # # # # #         print("Student Added!")

    
# # # # # #     elif choice == "2":
# # # # # #         if len(students) == 0:
# # # # # #             print("No records found")
# # # # # #         else:
# # # # # #             for roll in students:
# # # # # #                 print("Roll:", roll,
# # # # # #                       "Name:", students[roll]["name"],
# # # # # #                       "Marks:", students[roll]["mark"])

# # # # # #     elif choice == "3":
# # # # # #         roll = input("Enter Roll No: ")

# # # # # #         if roll in students:
# # # # # #             print("Found:", students[roll])
# # # # # #         else:
# # # # # #             print("Student not found")

   
# # # # # #     elif choice == "4":
# # # # # #         roll = input("Enter Roll No: ")

# # # # # #         if roll in students:
# # # # # #             del students[roll]
# # # # # #             print("Deleted successfully")
# # # # # #         else:
# # # # # #             print("Student not found")

  
# # # # # #     elif choice == "5":
# # # # # #         print("Exiting...")
# # # # # #         break

# # # # # #     else:
# # # # # #         print("Invalid choice")


# # # # # def last_word_length(text,):

# # # # #     words = text.split()     
# # # # #     last_word = words[-1]     
# # # # #     return last_word, len(last_word)

# # # # # text ="luffy is still joyboy"
# # # # # text1 ="hello world"
# # # # # text2 ="   fly me   to   the moon "
# # # # # word, length = last_word_length(text)


# # # # # print("Last word:", word)
# # # # # print("Length:", length)




# # # # # def lengthOfLastWord(s):
# # # # #     words = s.split()
# # # # #     print(words)  
# # # # #     print( "number of letters in last word :")       
# # # # #     return len(words[-1])      


# # # # # print(lengthOfLastWord("Hello World"))                  
# # # # # print(lengthOfLastWord("   fly me   to   the moon  "))  
# # # # # print(lengthOfLastWord("luffy is still joyboy"))  


# # # # a=int(input("enter a number : "))
# # # # b=int(input("enter a number : "))
# # # # c=a/b
# # # # print(c)


# # # try:
# # #   a=int(input("enter a number"))
# # #   b=int(input("enter a number"))
# # #   c=a/b
# # #   print(c)
# # # except:  
# # #     print("Error occured")


# # try:
# #     a = 10 / 0
# # except Exception as e:
# #     print("Error:", e)

# # try:
# #   f = open("demofile.txt","w")
# #   print("File opened successfully")
# #   try:
# #     f.write("lorum ipsom")
# #     print("File written successfully")
# #   except:
# #     print("Something went wrong when writing to the file")
# #   finally:
# #     f.close()
# # except:
# #   print("Something went wrong when opening the file")


# def split_odd_even(word):
    
#     even_place = word[::2]  
#     odd_place = word[1::2]  
#     return even_place, odd_place

# name = "ocdefg"
# even_chars, odd_chars = split_odd_even(name)

# print(f"Even places: {even_chars}") 
# print(f"Odd places: {odd_chars}")   



# name=input("")
# odd=""
# even=""
# result=""
# for index,value in enumerate(name,start=1):
#     if index % 2 != 0:
#         odd=odd+value
#     else:
#         even=even+value
# result = odd +" "+ even
# print(result)


# f = open("file.txt", "r")
# print(f.read())   
# f.close()
# f = open("file.txt", "w")
# f.write("Hello NIKHIL!!")
# f=open("file.txt","a")
# f.write("\nwelcome to python file handling")
# f.close()




# ext="CodEkaTa"
# print(text.swapcase())


# name=input()
# result=""
# for i in name:
#     if i.islower():
#         result=result+i.upper()
#     elif i.isupper():
#         result=result+i.lower()
#     else:
#         result=result+i
# print(result)



# name=input("enter you name: ")
# count=0
# for i in name:
#     count=count+1       
# print(count)


# day=input("enter the day : ")
# day=day.lower()
# if day=="sunday" or day=="saturday":
#     print("yes")
# else:    
#     print("no")  
 
# name=input("enter your name : ")
# unique_chars=set(name)
# print("Unique characters in the name:", unique_chars)


# a=input("enter a word to check whether it is a palindrome : ")
# if a==a[::-1]:
#     print("yes it is a palindrome") 
# else:    
#     print("no it is not a palindrome")



# import qrcode
# from PIL import Image
# data = "https://github.com"
# qr = qrcode.make(data)
# qr.show()



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("prakash", 19)
# s2 = Student("Nikhil", 18)
# s1.display()
# s2.display()  



# class series:
#         def __init__(self):
#            self.name = input("enter the name of the series : ")
#            self.genre = input("enter the genre of the series : ")   
#            self.year = input("enter the year of the series : ")

#         def display(self):
#             print("Name:", self.name)
#             print("Genre:", self.genre)
#             print("Year:", self.year)

# s1 = series()
# s2 = series()  
# print("-----") 
# s1.display()
# print("-----")
# s2.display()


# class student:
#     def __init__(self):
#         self.name = input("enter the name of the student : ")
#         self.rollno = input("enter the roll number of the student : ")   
#         self.mark = input("enter the mark of the student : ")

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.rollno)
#         print("Mark:", self.mark)       
# s1 = student()
# s2 = student()  
# print("-----")
# s1.display()    
# print("-----")
# s2.display()    



# def check_password_strength(pwd):
#     import re
#     if (len(pwd) >= 8 and
#         re.search(r"[A-Z]", pwd) and
#         re.search(r"[a-z]", pwd) and
#         re.search(r"[0-9]", pwd) and
#         re.search(r"[!@#$%^&*()_+]", pwd)):
#         return "Strong"
#     return "Weak"

# print(check_password_strength("Hello123"))


