
Name = input("Name : ")

Maths = int(input("Maths : "))
if Maths <0 or Maths>100 :
    print("invalid input")

English = int(input("English : "))
if English <0 or English>100 :
    print("invalid input")


Kiswahili = int(input("Kiswahili : "))
if Kiswahili <0 or Kiswahili>100 :
    print("invalid input")


Science = int(input("Science : "))
if Science <0 or Science>100 :
    print("invalid input")


Sst = int(input("Sst : "))
if Sst <0 or Sst>100 :
    print("invalid input")




Total_marks = int(Maths) + int(English) + int(Kiswahili) + int(Science) + int(Sst)

print(Total_marks)


average_marks = Total_marks/5
print (average_marks)

if average_marks >=100:
    print("Invalid input".format(average_marks))

elif (average_marks >=79 <=100 ):     #A = > 79 , B - 60 to 78, C - 59 to 49, D - 48 to 40, E - less 40

    print("Mean grade = A".format(average_marks))

elif average_marks >=60 <=78 :
    print("Mean grade = B".format(average_marks))

elif average_marks >=49 <=59 :
    print("Mean grade = C".format(average_marks))

elif average_marks >=40 <=48 :
    print("Mean grade = D".format(average_marks))

elif average_marks >=0 <40 :
    print("Mean grade = E".format(average_marks))

elif average_marks <0 :
    print("Invalid input".format(average_marks))




