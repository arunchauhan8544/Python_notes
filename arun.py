#print('Hello World')
#python program to declare variables
#mynumber = 3
#print(mynumber)

#mynumber2 = 4.5
#print(mynumber2)

#mynumber ="helloworld"
#print(mynumber)

#python program to demonstrate numeric value

##print("type of a: ", type(a))

#b = 5.0
#print("\nType of b: ", type(b))

#c = 2+4j
#print("\nType of c: ", type(c))

#print('We all are {}.'.format('equal'))

#print('{2} {1} {0}'.format('direction','the','read'))

#print('a: {a}, b: {b}, c: {c}'.format(a = 1,b = 'Two',c = 12.3))







#print('The valueof pi is: %1.5f' %3.141592) 
#print('The valueof pi is: {0:1.5f}'.format(3.141592))


#name = 'Ele'
#print(f"My name is {name}.")

#a = 5
#b = 10
#print(f"He said his age is {2 * (a + b)}.") 

#num = 3.14159
#print(f"The valueof pi is: {num:{1}.{5}}")

#from string import Template
 
#n1 = 'Hello'
#n2 = 'GeeksforGeeks'
 
# made a template which we used to pass two variable so n3 and n4 formal and n1 and n2 actual
#n = Template('$n3 ! This is $n4.')
 
# and pass the parameters into the template string.
#print(n.substitute(n3=n1, n4=n2))

#string = "GeeksForGeeks!"
#width = 30
 
#centered_string = string.center(width)
 
#print(centered_string)



#string = 'random'

#print("index of 'and' in string:", string.index('and'))

# initializing target string 
#ch = "geeksforgeeks"
  
# initializing argument string 
#ch1 = "geeks"
  
# using index() to find position of "geeks" starting from 2nd index prints 8
#pos = ch.index(ch1,2) 
  
#print("The first position of geeks after 2nd index : ",end="")
#print(pos)

#test_string = "1234gfg4321"
# finding gfg in string segment 'gfg4'
#print(test_string.index('gfg', 4, 8))
  
# finding "21" in string segment 'gfg4321'
#print(test_string.index("21", 8, len(test_string)))
  
# finding "32" in string segment 'fg432' using negative index
#print(test_string.index("32", 5, -1))

#text = "Hello Geeks and welcome to Geeksforgeeks"
#substring_list = ["Geeks", "welcome", "notfound"]
  
#indices = [text.index(sub) if sub in text else -1 for sub in substring_list]
#print(indices) 

#3tuple1 = (0, 1, 2, 3)
#tuple1[0] = 4
#print(tuple1)

#my_list = [1, 2, 3]
#my_list.append(4)
#print(my_list)
 
#my_list.insert(1, 5)
#print(my_list)
 
#my_list.remove(2)
#print(my_list)
 
##popped_element = my_list.pop(0)
#print(my_list)        
#print(popped_element)

#my_dict = {"name": "Tezz", "age": 22}
#new_dict = my_dict
#new_dict["age"] = 37
 
#print(my_dict)  
#print(new_dict)

#print(bool("Hello"))
#print(bool(15))


#thislist = list(("apple", "banana", "cherry")) 
#print(thislist)

#Lst = [50,70,30,30,90,10,50]

#Display list
#print(Lst[-7::1])

# Initialize list
#List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Show original list
#print("Original List:\n", List)
 
#print("\nSliced Lists: ")
 
# Display sliced list
#print(List[3:9:2])
 
# Display sliced list
#print(List[::2])
 
# Display sliced list
#print(List[::])

#matrix = [[1, 2, 3, 4],
 #   [5, 6, 7, 8],
  #  [9, 10, 11, 12]]
#

#print("Matrix =", matrix)


#my_list

#my_list = ['geeks', 'for']

#Add geeks to the list

#my_list.append('geeks')
#print(my_list)

# A sample function that takes 4 arguments
# and prints the,
#def fun(a, b, c, d):
 #   print(a, b, c, d)
 
# Driver Code
#my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
#fun(*my_list)

#def mySum(*args):
 #   		return sum(args)
 
# Driver code
#print(mySum(1, 2, 3, 4, 5))
#print(mySum(10, 20))

#def check_return():
 #   pass
#print(check_return())

#print(type(None))
#print(type(Null))


#Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
#print(Dict)


# Creating a Dictionary with Integer Keys
#Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
#print("\nDictionary with the use of Integer Keys: ")
#print(Dict)
  
# Creating a Dictionary with Mixed keys
#Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
#print("\nDictionary with the use of Mixed Keys: ")
#print(Dict)


# Creating a Dictionary
#Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using key
#print("Accessing a element using key:")
#print(Dict['name'])
  
# accessing a element using key
#print("Accessing a element using key:")
#print(Dict[1])

# Creating a Dictionary
#Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
#print("Dictionary =")
#print(Dict)
#Deleting some of the Dictionar data
#del(Dict[1]) 
#print("Data after deletion Dictionary=")
#print(Dict)

#var = ("Geeks", "for", "Geeks")
#print(var)

#values : tuple[int | str, ...] = (1,2,4,"Geek")
#print(values)

#mytuple = ("Geeks",)
#print(type(mytuple))
 
#NOT a tuple
#mytuple = ("Geeks")
#print(type(mytuple))

#tuple_constructor = tuple(("dsa", "developement", "deep learning"))
#print(tuple_constructor)


#var = {"Geeks", "for", "Geeks"}
#print(type(var))

#myset = set(["a", "b", "c"])
#print(myset)
 


#myset.add("d")
#print(myset)

#myset = {"Geeks", "for", "Geeks"}
#print(myset)
 
#myset[1] = "Hello"
#print(myset)


#people = {"Jay", "Idrish", "Archi"}
#people.add("Daxit")
#print(people)


#people = {"Jay", "Idrish", "Archil"}
#vampires = {"Karan", "Arjun"}
#dracula = {"Deepanshu", "Raju"}
 
#population = people.union(vampires)
 
#print("Union using union() function")
#print(population)
 
#population = people|dracula
 
#print("\nUnion using '|' operator")
#print(population)


#set1 = {1,2,3}
#set2 = {1,2,3}
#set3 = set1.intersection(set2)
#print(set3)
#set3 = set1 & set2
#print(set3)

#set1 = {1,2,3,4,5,6}
#set1.clear()
#print(set1)
	


#a = 33
#b = 200
#if b > a:
 #    print("b is greater than a")


#a = 200
#b = 33
#if b > a:
  #print("b is greater than a")
##elif a == b:
  #print("a and b are equal")
#else:
 # print("a is greater than b")

 # Since all are false, false is returned
#print (any([False, False, False, False]))
 
# Here the method will short-circuit at the
# second item (True) and will return True.
#print (any([False, True, False, False]))
 
# Here the method will short-circuit at the
# first (True) and will return True.
#print (any([True, False, False, False]))




# Here all the iterables are True so all
# will return True and the same will be printed
#print (all([True, True, True, True]))
 
# Here the method will short-circuit at the
# first item (False) and will return False.
#print (all([False, True, True, False]))
 
# This statement will return False, as no
# True is found in the iterables
#print (all([False, False, False]))


# Python program to demonstrate logical or operator  
#a = 10
#b = -10
#c = 0  
#f a > 0 or b > 0: 
#    print("Either of the number is greater than 0") 
#else: 
 #   print("No number is greater than 0") 
#if b > 0 or c > 0: 
 #   print("Either of the number is greater than 0") 
#else: 
 #   print("No number is greater than 0") 




#list1 = []
#list2 = []
#list3 = list1
 
# case 1
#if (list1 == list2):
 #   print("True")
#else:
 #   print("False")
 
# case 2
#if (list1 is list2):
 #   print("True")
#else:
 #   print("False")
 
# case 3
#if (list1 is list3):
 #   print("True")
#else:   
 #   print("False")
     
# case 4
#list3 = list3 + list2
 
#if (list1 is list3):
 #   print("True")
#else:   
 #   print("False")


#count = 0
#while (count < 3):
 #   count = count + 1
  #  print("Hello Geek")

#count = 0
#while (count < 3):
 #   count = count + 1
  #  print("Hello Geek")
#else:
 #   print("In Else Block")

#n = 4
#for i in range(0, n):
 #   print(i)


#print("List Iteration")
#l = ["geeks", "for", "geeks"]
#for i in l:
  #  print(i)
 
# Iterating over a tuple (immutable)
#print("\nTuple Iteration")
#t = ("geeks", "for", "geeks")
#for i in t:
 #   print(i)
 
# Iterating over a String
#print("\nString Iteration")
#s = "Geeks"
#for i in s:
   # print(i)
 
# Iterating over dictionary
#print("\nDictionary Iteration")
#d = dict()
#d['xyz'] = 123
#d['abc'] = 345
#for i in d:
 #   print("%s  %d" % (i, d[i]))
 
# Iterating over a set
#print("\nSet Iteration")
#set1 = {1, 2, 3, 4, 5, 6}
#for i in set1:
 #   print(i),


#x = range(3, 20, 2)
#for n in x:
 #   print(n)

#l1 = ["eat", "sleep", "repeat"]
#s1 = "geek"
 
# creating enumerate objects
#obj1 = enumerate(l1)
#obj2 = enumerate(s1)
 
#print ("Return type:", type(obj1))
#print (list(enumerate(l1)))
 
# changing start index to 2 from 0
#print (list(enumerate(s1, 2)))

#s = 'geeksforgeeks'
# Using for loop
#for letter in s:
  
 #   print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
  #  if letter == 'e' or letter == 's':
   #     break
  
#print("Out of for loop")
#print()
  
#i = 0
  
# Using while loop
#while True:
 #   print(s[i])
  
    # break the loop as soon it sees 'e'
    # or 's'
  #  if s[i] == 'e' or s[i] == 's':
   #     break
    #i += 1
  
#print("Out of while loop")


# Python program to
# demonstrate continue
# statement
  
# loop from 1 to 10
#
#
#o 6,
# iteration
#
#
#
#
#int the value
#
# " ")


# Python program to demonstrate
# pass statement
  
#s = "geeks"
#  
## Empty loop
#for i in s:
#    # No error will be raised
#    pass
#  
## Empty function
#def fun():
#    pass
#  
## No error will be raised
#fun()
#  
## Pass statement
#for i in s:
#    if i == 'k':
#        print('Pass executed')
#        pass
#    print(i)
#

#def my_function(fname):
#  	print(fname + " Refsnes")
#

#

#
# my_function("Emil")
#
# my_function("Tobias")
#
# my_function("Linus")
#

#def my_function(*kids):
#  print("The youngest child is " + kids[2])
#my_function("Emil", "Tobias", "Linus")
#
#def my_function(**kid):
#  print("His last name is " + kid["lname"])
#my_function(fname = "Tobias", lname = "Refsnes")
#

#def my_function(country = "Norway"):
#  	print("I am from " + country)
#my_function("Sweden")
#my_function("India")
#my_function()
#my_function("Brazil")
#

#def my_function(x):
#  return 5 * x
#print(my_function(3))
#print(my_function(5))
#
#def my_function():
#    '''Demonstrates triple double quotes
#    docstrings and does nothing really.'''
#  
#    return None
# 
#print("Using __doc__:")
#print(my_function.__doc__)
# 
#print("Using help:")
#help(my_function)
#

#x = 15
#def change():
#    # using a global keyword
#    global x
#    # increment value of x by 5 
#    x = x+5
#    print("Value of x inside a function :", x)
#
#change()
#print("Value of x outside a function :", x)

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
	x = "hello"
  myfunc2()
  return x
print(myfunc1())
