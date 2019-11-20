taskList = [23, "jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
#z="jane"
#print(type(z))
#y={"currency" : "KES"}
#print(type(y))
print(type(taskList))


print(taskList[2][2]['currency'])
print(taskList[2][1])

x = len(taskList)
print(x)

print(str(taskList[3])[::-1])
n=str(taskList)
print(n)
print (n.replace("John", "jane"))
