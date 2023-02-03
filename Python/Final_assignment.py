
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
def div_by_7_but_not_by_5():
	list_of_numbers = []
	for i in range(2000, 3201):
		if i%7 == 0 and i%5!=0:
			list_of_numbers.append(i)
	
	print("\n1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).\n")
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
	print("\n3. Convert a number into binary and binary to number.")
	n = int(input("Enter a number to convert it into binary: "))
	binarynum = bin(n).replace("0b", "")
	print("The binary of", n ,"is", binarynum)
	print("The number of", binarynum, "this binary is", int(binarynum, 2) ,"\n")


# 4.Reverse the list by using negative index and apply logic also.
def rev_list():
    print("\n4. Reverse the list by using negative index and apply logic also.")
    list = ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil']
    new_list = []
    for i in range(len(list)-1 , -1, -1):
        new_list.append(list[i])
    
    print(list)
    print(new_list)
    print()


'''
5. participants_list = [['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']] '''
# print("daily_participants---------")
# daily_participants(participants_list) 
# # ['Desmond', 'Krish', 'Sam']
# print("one_time_participants---------")
# one_time_participants(participants_list)
# # ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
# print("first_day_only_participants----------------")
# first_day_only_participants(participants_list) #  ['John', 'Joan']

def participations():
    def daily_participants(d, pl):
        daily_comers = []
        for participant, participation in d.items():
            if participation == len(pl):
                daily_comers.append(participant)
        
        return daily_comers

    def one_time_participants(d, pl):
        one_timers = []
        for participant, participation in d.items():
            if participation == 1:
                one_timers.append(participant)

        return one_timers

    def first_day_only_participants(d, pl):
        bored_participants = []
        for i in pl[0]:
            if i in d and d[i] == 1:
                bored_participants.append(i)
        
        return bored_participants


    participants_list = [['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ], ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'], ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'], ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'], ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'], ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']]

    d = {}
    for i in participants_list:
        for j in i:
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1

    print("\n5. Play around with the list and printing the following : ")
    print("Daily Participants---------------------------\n", daily_participants(d, participants_list))
    print("One time Participants------------------------\n", one_time_participants(d, participants_list))
    print("Only First day Participants------------------\n", first_day_only_participants(d, participants_list))
    print()


# 6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.

def zig_zag():

    print("\n6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.s")
    first_list , second_list , third_list = [0,1,2,3,4,5,6,7,8,9] , [0,9,8,7,6,5] , []
    l = min(len(second_list), len(first_list))

    for i in range(l):
        if i%2 == 0: third_list.append(second_list[i])
        else: third_list.append(first_list[i])
    
    if l == len(first_list): third_list += second_list[l+1:]
    else: third_list += first_list[l+1:]
    
    print(third_list)
    print()




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
rev_list()
participations()
zig_zag()