# temperature = 10
# if temperature > 30:
#     print("its a hot day")

# elif temperature >20: 
#     print ("Its a nice day")

 
# else:
#     print(" good day by waether")      


# weight = int (input("Weight is:"))
# unit = str(input ("K or (L)bs:"))
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print ("Weight in Lbs :" + str (converted))

# else: 
#     converted = weight * 0.45
#     print ("weight is :" +str(converted))    


# i = 1
# while i <= 10:
#     print (i * '*')
#     i = i + 1
   
  


# for number in range(5, 10, 2):
#     print (number)

# cars = ["prado", "volvo", "jeep"]
# x = cars.copy()
# print(x)

# a = "Hello, World!"
# print(a.lower())

# a = " Hello,World!    "
# print(a.strip())


# a = "Hello, World!"
# print(a.split("o"))



# age =36
# txt = "My name is John, and I am {}"
# print(txt.format(age))


# txt = 'it\'s very bad'
# print(txt)

# txt = "This will insert one \ (backslash)."
# print(txt) 

# txt = "My name is Emdd"

# x = txt.encode()

# print(x)


# txt = "Hello, welcome to my world"

# x = txt.endswith("world")

# print(x)


# txt = "H\te\tl\tl\to"

# x =  txt.expandtabs(2)

# print(x)


# myTuple = ("John", "Peter", "Vicky")

# x = "+".join(myTuple)

# print(x)


# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


# x = 11

# x &= 2

# print(x)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# def myfunc(n):
#     return abs(n - 23)
# thislist = [23,34,23,67]
# thislist.sort(key=myfunc)
# print (thislist)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[1:4])


# thistuple = ("a", "b", "c")
# y = list(thistuple)
# y.append("d") 
# thistuple = tuple(y)
# print(thistuple)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set2.union(set1)
# print(set3)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.update({"brand": "foos"})

# print(thisdict)

# def myfunc(name,  roll, address):
#     print("I am a " + name, "my roll is" + int(roll), "address is "+ address)
# myfunc("Emon", int(34), "jatrabari")   

# def myfunc(n):
#   return lambda a : a + n

# mytripler = myfunc(3)

# print(mytripler(10))


# class Myclass:
#     y = 10
# m = Myclass()   
# print(m.y)


# class Person:
#   def __init__(self, name, age):
#      self.name = name
#      self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# class Computer:
#     def __init__(self, hardware, software):
#         self.hardware = hardware
#         self.software = software
#     def result(abc):
#       print("this is a" +abc.hardware)
# p = Computer("djdjdjd", "sjdshshsh")
# p.result()      


# class Parent:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name 
#     def method1(self):
#         print("Father name is " + self.name+ self.age )    

# class Daughter(Parent): 
#  pass 
# x = Daughter("HSujsh", "dkhwdj")
# x.method1()
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class Parent:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#        x =self.a
#        self.a += 1
#        return x
# myclass = Parent()      
# myiter = iter(myclass) 

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
import module
import datetime


# a = module.person1["age"]
# print(a)

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))
# x = datetime.datetime(2020, 5, 17)

# print(x)
import math

x = math.pi

print(x)