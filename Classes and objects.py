# name = "JB"
# age = 20
# print(type(age))

# class Person :
#     #class attributes
#     #species = "Homo Sapiens"
#
#     def walk(self):
#         print("{} is walking ".format(self.name))
#
#     def sleep(self):
#         print("rarely sleeps")
#
#     def eating(self):
#         print("eats a lot")
#
#     def working(self):
#         print("works hard")
#
#
# p1 = Person()
# p1.name = "JB"
# #
# # p1.name = "jb"
# #
# p1.walk()
# p1.sleep()
# p1.working()

#  print(p1.species)
#  p1.name = "JB"
# p1.age = 23
# print(p1.age)
# p1.marriege = "single"
# print(p1.marriege)
# p1.gender = education)"Male"
# print(p1.gender)
# p1.level_of_education = "University"
# print(p1.level_of_
#
#
# p2 = Person()
# print(p2.species)
# p1.name = "kay"
# print(p1.name)
# p1.age = 20
# print(p1.age)
# p1.marriege = "Divorced"
# print(p1.marriege)
# p1.gender = "Female"
# print(p1.gender)
# p1.level_of_education = "Primary"
# print(p1.level_of_education)
#
#
# p3 = Person()
# print(p3.species)
#
# p4 = Person()
# print(p4.species)

# class Car:
#     def model(self):
#         print("{} V12 ".format(self.name))
#
#     def color(self):
#         print("yellow green")
#
#     def road_use(self):
#         print("4Wd")
#
#     def rims(self):
#         print("expensive rims")
#     def price(self):
#         print("$100,000")
#
#
# c1 = Car()
# c1. name = "Aston Matin"
# c1.model()
# c1.color()
# c1.road_use()
# c1.price()
# c1.rims()


class Person:

    def __init__(self,name,age):#it runs as soon as object is created
        print("i am a genius")
        self.name = name
        self.age = age

    def eating(self):
        print("{} is walking ".format(self.name).format(self.age))
Jb = Person("JINA",30)
print(Jb.name)
print(Jb.age)
Jb.eating()

class Student:
    def __init__(self,school_name,name,grade):