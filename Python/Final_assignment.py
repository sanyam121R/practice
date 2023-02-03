
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
def div_by_7_but_not_by_5():
	list_of_numbers = []
	for i in range(2000, 3201):
		if i%7 == 0 and i%5!=0:
			list_of_numbers.append(i)
	
	print("1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).")
	print(list_of_numbers ,"\n")


# 2. get the occurence of all vowels and consonent from the large given string.
def vowels_consonent_string(s):
	vowels = ['a', 'e', 'i', 'o', 'u']
	consonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	v_st , c_st = "" , ""
	for i in s:
		if i in vowels:
			v_st += i
		elif i in consonent:
			c_st += i
	print("\n2. Get the occurence of all vowels and consonent from the large given string.")
	print("There are" , len(v_st), "vowels = ", v_st )
	print("There are" , len(c_st), "consonents = ", c_st ,"\n")


# 3. convert a number into binary and binary to number.
def binary_to_number():
	print("3. Convert a number into binary and binary to number.")
	n = int(input("Enter a number to convert it into binary: "))
	binarynum = bin(n).replace("0b", "")
	print("The binary of", n ,"is", binarynum)
	print("The number of", binarynum, "this binary is", int(binarynum, 2) ,"\n")


# 4.Reverse the list by using negative index and apply logic also.

def rev_list():
	pass

'''
5. participants_list = [
      ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
      ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
      ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
      ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
      ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
      ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]
'''

# print("daily_participants---------")
# daily_participants(participants_list) 
# # ['Desmond', 'Krish', 'Sam']

# print("one_time_participants---------")

# one_time_participants(participants_list)
# # ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']

# print("first_day_only_participants----------------")
# first_day_only_participants(participants_list) #  ['John', 'Joan']

# 6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.

# 7. Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by using list comprehension 

# dict ={"key1":1234, "k2":"ram"}
# list= [1234,"ram"]

# 8. Access the nested key ‘salary’ from the following JSON
'''
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
   { 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
   { 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

'''
# emp-id     emp-name -- salary


# 9. Create class OOPS and implement all oops concept in that.

# 10. Create a class BANK and with two function simple interest and compound interest. U need to create instance for pnb, icici and hdfc banks with corresponding input.




div_by_7_but_not_by_5()
vowels_consonent_string('asdfsadgaswero')
binary_to_number()