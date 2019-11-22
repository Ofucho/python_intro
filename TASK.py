# if 1000 is True :
#     print("login success")
# elif not 1000 :
#     print("wrong")


#
# # i=range(3)
# # print
#
Pin = 1000
attempts = 3
x = 1

while x<=3:

     pin = int(input("Enter Pin : "))

     if  pin!=Pin :

         attempts=attempts-1
         if attempts ==0:

            print("SIM blocked")

         else:
            print("Wrong! You have {} attempts left!".format(attempts))
            x=+1
     else:
             print("Login Success!")

             break